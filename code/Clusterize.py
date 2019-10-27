import numpy as np
from skimage import transform, color
from sklearn.cluster import spectral_clustering
from sklearn.feature_extraction import img_to_graph

from Utils import visualize


class Clusterize:
    def __init__(self, image_list, graph_beta=10, graph_eps=1e-6, max_transform_size=None):
        self.image_list = image_list
        self.graph_eps = graph_eps
        self.graph_beta = graph_beta
        self.labels = None

        self.to_gray()

        if max_transform_size is not None:
            self.transform(max_transform_size)

        self.graph_list = self.make_graph()

    def transform(self, max_size) -> None:
        for i, image in enumerate(self.image_list):
            self.image_list[i] = transform.resize(image,
                                                  (np.array(image.shape) / np.max(image.shape) * max_size).astype(int))

    def to_gray(self) -> None:
        for i, image in enumerate(self.image_list):
            self.image_list[i] = color.rgb2gray(image)

    def make_graph(self) -> list:
        result = []
        for image in self.image_list:
            graph = img_to_graph(image)
            graph.data = np.exp(- self.graph_beta * graph.data / graph.data.std()) + self.graph_eps

            result.append(graph)

        return result

    @staticmethod
    def crop_by_mask(image, mask):
        crop = image.copy()
        crop[mask == False] = 0

        crop = crop[~(crop == 0).all(1)]
        crop = crop.T
        crop = crop[~(crop == 0).all(1)]
        return crop.T

    def apply(self, **kwargs) -> list:
        result = []

        for i, graph in enumerate(self.graph_list):
            image = self.image_list[i]
            self.labels = spectral_clustering(
                graph,
                **kwargs
            )
            self.labels = self.labels.reshape(image.shape)

            self.labels[image == 0] = -1

            for label_index in range(0, self.labels.max() + 1):
                result.append(
                    self.crop_by_mask(image, self.labels == label_index)
                )

        return result

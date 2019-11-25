"""@package core.AlgorithmList
@brief Алгоритмы сегментации, работающие с несколькими изображениями
"""

import numpy as np
from scipy.ndimage import gaussian_filter
from skimage import color, transform
from sklearn.cluster import spectral_clustering
from sklearn.feature_extraction import img_to_graph


class AlgorithmList:
    """Родительский класс для реализаций алгоритмов сегментации (со списком изображений)
    """

    ## Целевые изображения
    image_list = None

    def __init__(self, image_list, max_transform_size=None):
        """Инициализация алгоритма

Копирует переданные изображения

@param image_list: Изображения для обработки
@param max_transform_size: Максимальный размер изображения
Если изображение больше этого размера - оно сжимается
        """
        self.image_list = [i.copy() for i in image_list]

        self.to_gray()
        self.remove_noise()

        if max_transform_size is not None:
            self.transform(max_transform_size)

    def to_gray(self):
        """Преобразование изображений в оттенки серого
        """
        for i, image in enumerate(self.image_list):
            self.image_list[i] = color.rgb2gray(image)

    def remove_noise(self, level=2):
        """Медианный алгоритм для уменьшения шумов
        @param level: Радиус диска (ядра)
        """
        for i, image in enumerate(self.image_list):
            self.image_list[i] = gaussian_filter(image, sigma=2)

    @staticmethod
    def crop_by_mask(image, mask):
        """Максимально возможное кадрирование изображения после наложения маски
        @return Кадрированное изображение
        """
        crop = image.copy()
        crop[mask == False] = 0

        crop = crop[~(crop == 0).all(1)]
        crop = crop.T
        crop = crop[~(crop == 0).all(1)]
        return crop.T

    def transform(self, max_size):
        """Уменьшение разрешения изображения, если исходное больше заданного
        @param max_size: Заданное максимальное разрешение
        """
        for i, image in enumerate(self.image_list):
            if np.min(image.shape) <= max_size:
                continue

            self.image_list[i] = transform.resize(image,
                                                  (np.array(image.shape) / np.max(image.shape) * max_size).astype(int),
                                                  mode='reflect')


class SpectralClustering(AlgorithmList):
    """Реализация алгоритма спектральной кластеризации
    """

    ## Константа нормирования весов графа, множитель степени экспоненты
    graph_beta = None

    ## Константа нормирования весов графа, сдвиг степени экспоненты
    graph_eps = None

    ## Список преобразованных в графы изображений
    graph_list = None

    ## Список изображений, характеризующих разбиение на кластеры
    labels_result = None

    def __init__(self, image_list, graph_beta=10, graph_eps=1e-6, max_transform_size=None):
        """
        @copydoc AlgorithmList::\_\_init\_\_()
        @param graph_beta: Константа формулы построения графа: бета
        @param graph_eps: Константа формулы построения графа: эпсилон
        """
        super().__init__(image_list, max_transform_size)

        self.graph_beta = graph_beta
        self.graph_eps = graph_eps

        self.graph_list = self.make_graph()
        self.labels_result = []

    def make_graph(self):
        """Создание графов
        @return Список графов, причем индекс графа совпадает с индексом изображения
        """
        result = []
        for image in self.image_list:
            graph = img_to_graph(image)
            graph.data = np.exp(- self.graph_beta * graph.data / graph.data.std()) + self.graph_eps

            result.append(graph)

        return result

    def apply(self, **kwargs):
        """Максимально возможное кадрирование изображения после наложения маски

Именные параметры передаются в
<a href="https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html">
sklearn.cluster.spectral.spectral_clustering</a>

@return Список кластеризованных изображений
        """

        result = []

        for i, graph in enumerate(self.graph_list):
            image = self.image_list[i]

            labels = spectral_clustering(
                graph,
                **kwargs
            )

            labels = labels.reshape(image.shape)
            labels[image == 0] = -1

            print('Spectral clustering complete for', i)

            for label_index in range(0, labels.max() + 1):
                result.append(
                    self.crop_by_mask(image, labels == label_index)
                )

            self.labels_result.append(labels)

        return result

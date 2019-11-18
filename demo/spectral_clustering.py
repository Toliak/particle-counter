from math import ceil

import matplotlib.pyplot as plot
from skimage.exposure import adjust_sigmoid

import Dataset
from AlgorithmList import SpectralClustering

from Utils import visualize
from ImageChecker import is_atomic, label_peak_list


def display_all(images, size):
    plot.figure(figsize=size)

    row_amount = ceil(len(images) / 5)
    for i, img in enumerate(images):
        plot.subplot(row_amount, 5, i + 1)
        plot.imshow(img)
        plot.title(f'image {i}')

    plot.show()


original = Dataset.easy()
# original = adjust_sigmoid(original)

ITERATIONS = 2
GRAPH_BETA = (5, 5, 5)
GRAPH_EPS = (1e-8, 0, 0)
N_CLUSTERS = (15, 15, 5)
N_INIT = (1, 1, 1)
LABELS = ('discretize', 'kmeans', 'discretize')
RESULT_OUTPUT_SIZE = ((10, 10), (15, 60), (10, 60))
FIRST_MAX_TRANSFORM_SIZE = None

result = [original]

for i in range(0, ITERATIONS):
    print('Clusterization iteration ', i)
    clusterize = SpectralClustering(result,
                            graph_beta=GRAPH_BETA[i],
                            graph_eps=GRAPH_EPS[i],
                            max_transform_size=FIRST_MAX_TRANSFORM_SIZE if i == 0 else None)

    if i == 0:
        visualize(clusterize.image_list[0], 'input')

    result = clusterize.apply(n_clusters=N_CLUSTERS[i],
                              n_init=N_INIT[i],
                              eigen_solver='amg',
                              assign_labels=LABELS[i],
                              random_state=1)

    display_all(result, RESULT_OUTPUT_SIZE[i])
    display_all(label_peak_list(result), RESULT_OUTPUT_SIZE[i])

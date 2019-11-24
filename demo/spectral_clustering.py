import os
import sys
from datetime import datetime
from math import ceil

import matplotlib.pyplot as plot

from Utils import get_artifact_path

sys.path.append('code')

import Dataset
from AlgorithmList import SpectralClustering

from ImageChecker import is_atomic, is_background, label_peak_amount


def display_all(images, size):
    plot.figure(figsize=size)

    row_amount = ceil(len(images) / 5)
    for i, img in enumerate(images):
        plot.subplot(row_amount, 5, i + 1)
        plot.imshow(img)
        plot.title(f'image {i}')

    plot.show()


original = Dataset.load_by_path('test.png')
# original = adjust_sigmoid(original)

ITERATIONS = 3
GRAPH_BETA = (15, 15, 15)
GRAPH_EPS = (1e-6, 1e-6, 1e-6)
N_CLUSTERS = (10, 5, 3)
N_INIT = (2, 2, 2)
LABELS = ('discretize', 'discretize', 'discretize')
RESULT_OUTPUT_SIZE = ((10, 10), (15, 30), (15, 30))
FIRST_MAX_TRANSFORM_SIZE = 256

final_particles = []
result = [original]

for i in range(0, ITERATIONS):
    print('Clusterization iteration ', i)
    clusterize = SpectralClustering(result,
                                    graph_beta=GRAPH_BETA[i],
                                    graph_eps=GRAPH_EPS[i],
                                    max_transform_size=FIRST_MAX_TRANSFORM_SIZE if i == 0 else None)

    if i == 0:
        plot.figure(figsize=(8, 8))
        plot.axis('off')
        plot.imshow(clusterize.image_list[0], cmap='viridis')
        plot.title('input')

        if not os.path.exists('../artifacts/'):
            os.makedirs('../artifacts/')
        plot.savefig(f'../artifacts/clustering_input_{datetime.now().timestamp()}.png',
                     bbox_inches='tight')

    result = clusterize.apply(n_clusters=N_CLUSTERS[i],
                              n_init=N_INIT[i],
                              eigen_solver='amg',
                              assign_labels=LABELS[i],
                              random_state=1)

    plot.figure(figsize=RESULT_OUTPUT_SIZE[i])

    remove_indexes = []

    row_amount = ceil(len(result) / 5) * 2

    for j, img in enumerate(result):
        is_bg = is_background(img)
        if is_bg:
            remove_indexes.append(j)

        plot.subplot(row_amount, 5, j * 2 + 1)
        plot.imshow(img)
        plot.title(f'image {j}\nbg: {is_bg}'
                   f'\natomic: {is_atomic(img): <07.6f}')

        if not is_bg:
            labels, amount = label_peak_amount(img)

            plot.subplot(row_amount, 5, j * 2 + 2)
            plot.imshow(labels)
            plot.title(f'image {j}\namount: {amount}')

            if amount == 0:
                remove_indexes.append(j)
            elif amount == 1:
                final_particles.append(img.copy())
                remove_indexes.append(j)

    plot.savefig(get_artifact_path(f'clustering_{i}_{datetime.now().timestamp()}'),
                 bbox_inches='tight')

    # Remove background-only images
    for index in sorted(remove_indexes, reverse=True):
        del result[index]

final_particles.extend(result)

plot.figure(figsize=(15, 15))
row_amount = ceil(len(final_particles) / 5)
for j, img in enumerate(final_particles):
    plot.subplot(row_amount, 5, j + 1)
    plot.imshow(img)

plot.savefig(get_artifact_path(f'clustering_output_{datetime.now().timestamp()}'),
             bbox_inches='tight')
print(f'Result amount: {len(final_particles)}')

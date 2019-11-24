import sys
from datetime import datetime
from math import ceil

import matplotlib.pyplot as plot

import config.config_spectral_clustering as config
from Utils import get_artifact_path


from ..code import Dataset
from ..code.AlgorithmList import SpectralClustering

from ImageChecker import is_atomic, is_background, label_peak_amount


def display_all(images, size):
    plot.figure(figsize=size)

    row_amount = ceil(len(images) / 5)
    for i, img in enumerate(images):
        plot.subplot(row_amount, 5, i + 1)
        plot.imshow(img)
        plot.title(f'image {i}')

    plot.show()


original = Dataset.load_by_path('test_cluster.png')

final_particles = []
result = [original]

for i in range(0, config.ITERATIONS):
    print('Clusterization iteration ', i)
    clusterize = SpectralClustering(result,
                                    graph_beta=config.GRAPH_BETA[i],
                                    graph_eps=config.GRAPH_EPS[i],
                                    max_transform_size=config.FIRST_MAX_TRANSFORM_SIZE if i == 0 else None)

    if i == 0:
        plot.figure(figsize=(8, 8))
        plot.axis('off')
        plot.imshow(clusterize.image_list[0], cmap='viridis')
        plot.title('input')

        plot.savefig(get_artifact_path(f'clustering_input_{datetime.now().timestamp()}'),
                     bbox_inches='tight')

    result = clusterize.apply(n_clusters=config.N_CLUSTERS[i],
                              n_init=config.N_INIT[i],
                              eigen_solver='amg',
                              assign_labels=config.LABELS[i],
                              random_state=config.RANDOM_STATE)

    plot.figure(figsize=config.RESULT_OUTPUT_SIZE[i])

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

if __name__ == '__main__':
    assert len(config.GRAPH_BETA) >= config.ITERATIONS
    assert len(config.GRAPH_EPS) >= config.ITERATIONS
    assert len(config.N_CLUSTERS) >= config.ITERATIONS
    assert len(config.N_INIT) >= config.ITERATIONS
    assert len(config.LABELS) >= config.ITERATIONS
    assert len(config.RESULT_OUTPUT_SIZE) >= config.ITERATIONS



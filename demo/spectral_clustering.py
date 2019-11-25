"""@package demo.spectral_clustering
@brief Демонстрационный модуль для алгоритма спектральной кластеризации
"""
import sys
from datetime import datetime
from math import ceil

import imageio
import matplotlib.pyplot as plot

import config.config_spectral_clustering as config

sys.path.append('..')


def zero_iteration(clustering):
    """Действия на 1й итерации
    @param clustering: Объект обертки алгоритма кластеризации
    """
    plot.figure(figsize=(8, 8))
    plot.axis('off')
    plot.imshow(clustering.image_list[0], cmap='viridis')
    plot.title('input')

    plot.savefig(get_artifact_path(f'clustering_input_{datetime.now().timestamp()}'),
                 bbox_inches='tight')


def result_processing(result, row_amount, final_particles):
    """Обработка промежуточного результата
    @param result: Список кластеризованных изображений
    @param row_amount: Количество строк в визуализации
    @param final_particles: Список с результирующими изображениями частиц
    @return Список отмеченных индексов на удаление
    """
    remove_indexes = []

    for j, img in enumerate(result):
        is_bg = is_background(img, config.BACKGROUND_MAX_GRAY, config.BACKGROUND_PERCENT)
        if is_bg:
            remove_indexes.append(j)

        plot.subplot(row_amount, 5, j * 2 + 1)
        plot.imshow(img)
        plot.title(f'image {j}\nbg: {is_bg}')

        if not is_bg:
            labels, amount = label_peak_amount(img, config.LABEL_PEAK_MIN_GRAY, config.LABEL_PEAK_MIN_SIZE)

            plot.subplot(row_amount, 5, j * 2 + 2)
            plot.imshow(labels)
            plot.title(f'image {j}\namount: {amount}')

            if amount == 0:
                remove_indexes.append(j)
            elif amount == 1:
                final_particles.append(img.copy())
                remove_indexes.append(j)

    return remove_indexes


def evaluate(image_path=None):
    """Демонстрация алгоритма спектральной кластеризации
    @param image_path: Пусть к изображению. Если None, то используется стандартное изображение
    """
    if image_path:
        original_image = dict(image=imageio.imread(image_path),
                              title=image_path)
    else:
        original_image = Dataset.load_by_path('test_cluster.png')

    final_particles = []  # Результирующие изображения частиц
    result = [original_image]  # Промежуточные изображения

    for i in range(0, config.ITERATIONS):
        print('Clusterization iteration ', i)
        clusterize = SpectralClustering(result,
                                        graph_beta=config.GRAPH_BETA[i],
                                        graph_eps=config.GRAPH_EPS[i],
                                        max_transform_size=config.FIRST_MAX_TRANSFORM_SIZE if i == 0 else None)

        if i == 0:
            zero_iteration(clustering=clusterize)

        result = clusterize.apply(n_clusters=config.N_CLUSTERS[i],
                                  n_init=config.N_INIT[i],
                                  eigen_solver='amg',
                                  assign_labels=config.LABELS[i],
                                  random_state=config.RANDOM_STATE)

        row_amount = ceil(len(result) / 5) * 2  # Количество строк в визуализации
        plot.figure(figsize=config.RESULT_OUTPUT_SIZE[i])

        remove_indexes = result_processing(result=result,
                                           row_amount=row_amount,
                                           final_particles=final_particles)
        plot.savefig(get_artifact_path(f'clustering_{i}_{datetime.now().timestamp()}'),
                     bbox_inches='tight')

        # Удаление отмеченных изображений
        for index in sorted(remove_indexes, reverse=True):
            del result[index]

    final_particles.extend(result)

    plot.figure(figsize=config.FIGSIZE)
    row_amount = ceil(len(final_particles) / 5)
    for j, img in enumerate(final_particles):
        plot.subplot(row_amount, 5, j + 1)
        plot.imshow(img)

    plot.savefig(get_artifact_path(f'clustering_output_{datetime.now().timestamp()}'),
                 bbox_inches='tight')
    print(f'Result amount: {len(final_particles)}')


if __name__ == '__main__':
    from core.Utils import get_artifact_path, is_background, label_peak_amount
    from core import Dataset
    from core.AlgorithmList import SpectralClustering

    assert len(config.GRAPH_BETA) >= config.ITERATIONS
    assert len(config.GRAPH_EPS) >= config.ITERATIONS
    assert len(config.N_CLUSTERS) >= config.ITERATIONS
    assert len(config.N_INIT) >= config.ITERATIONS
    assert len(config.LABELS) >= config.ITERATIONS
    assert len(config.RESULT_OUTPUT_SIZE) >= config.ITERATIONS

    if len(sys.argv) >= 2:
        evaluate(sys.argv[1])
    else:
        evaluate()

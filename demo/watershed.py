"""@package demo
Демонстрационный модуль для порогового алгоритма
"""
import os
from datetime import datetime

import matplotlib.pyplot as plot
from skimage.filters import threshold_isodata, threshold_mean, threshold_triangle, threshold_otsu

import Dataset
from Algorithm import Watershed


def evaluate():
    """Демонстрация алгоритма порогового фильтра"""
    dataset_list = Dataset.get_full_dataset()
    images_len = len(dataset_list)

    plot.figure(figsize=(10, 70))
    subplot_rows = images_len
    subplot_cols = 2
    plot.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.3,
                        wspace=0.35)

    for i, data in enumerate(dataset_list):
        image, title = data['image'], data['title']

        threshold = Watershed(image)

        subplot_index = i * subplot_cols + 1
        plot.subplot(subplot_rows, subplot_cols, subplot_index)
        plot.imshow(threshold.image)
        plot.axis('off')
        plot.title(f'Grayscale {title}')

        result_image = threshold.apply()

        subplot_index = i * subplot_cols + 2
        plot.subplot(subplot_rows, subplot_cols, subplot_index)
        plot.imshow(result_image)
        plot.axis('off')
        plot.title(f'Result {title}\n'
                   f'Amount: {threshold.particle_amount}')

        print(f'Complete {title}')

    if not os.path.exists('../artifacts/'):
        os.makedirs('../artifacts/')
    plot.savefig(f'../artifacts/watershed_{datetime.now().timestamp()}.png',
                 bbox_inches='tight')


if __name__ == '__main__':
    evaluate()

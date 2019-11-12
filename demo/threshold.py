"""@package demo
Демонстрационный модуль для порогового алгоритма
"""
import os
from datetime import datetime

import matplotlib.pyplot as plot
from skimage.filters import threshold_isodata, threshold_mean, threshold_triangle, threshold_otsu

import Dataset
from Threshold import Threshold


def evaluate():
    dataset_list = Dataset.get_full_dataset()
    images_len = len(dataset_list)

    functions = [threshold_isodata,
                 threshold_mean,
                 threshold_triangle,
                 threshold_otsu]

    plot.figure(figsize=(20, 70))
    subplot_rows = images_len
    plot.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.3,
                        wspace=0.35)
    subplot_cols = len(functions) + 1

    for i, data in enumerate(dataset_list):
        image, title = data['image'], data['title']

        threshold = Threshold(image)

        subplot_index = i * (len(functions) + 1) + 1
        plot.subplot(subplot_rows, subplot_cols, subplot_index)
        plot.imshow(threshold.image)
        plot.axis('off')
        plot.title(f'Grayscale {title}')

        for j, f in enumerate(functions):
            result_image = threshold.apply_threshold(f)

            subplot_index = i * (len(functions) + 1) + 2 + j
            plot.subplot(subplot_rows, subplot_cols, subplot_index)
            plot.imshow(result_image)
            plot.axis('off')
            plot.title(f'Result {title} {f.__name__}\n'
                       f'Amount: {threshold.particle_amount}\n'
                       f'Threshold value: {threshold.threshold_value: 08.4f}')

    if not os.path.exists('../artifacts/'):
        os.makedirs('../artifacts/')
    plot.savefig(f'../artifacts/threshold_{datetime.now().timestamp()}.png',
                 bbox_inches='tight')


if __name__ == '__main__':
    evaluate()

"""@package demo.threshold
@brief Демонстрационный модуль для порогового алгоритма
"""
import sys
from datetime import datetime

import imageio
import matplotlib.pyplot as plot
from skimage.filters import threshold_isodata, threshold_mean, threshold_triangle, threshold_otsu

sys.path.append('..')


def evaluate(image_path=None):
    """Демонстрация алгоритма порогового фильтра
    @param image_path: Пусть к изображению. Если None, то используется стандартный датасет
    """
    if image_path:
        dataset_list = [dict(image=imageio.imread(image_path),
                             title=image_path)]
        images_len = len(dataset_list)
    else:
        dataset_list = Dataset.get_full_dataset()
        images_len = len(dataset_list)

    functions = [threshold_isodata,
                 threshold_mean,
                 threshold_triangle,
                 threshold_otsu]

    subplot_rows = images_len
    subplot_cols = len(functions) + 1

    plot.figure(figsize=config.FIGSIZE)
    plot.subplots_adjust(**config.SUBPLOT_ADJUST)

    for i, data in enumerate(dataset_list):
        image, title = data['image'], data['title']

        threshold = Threshold(image)

        subplot_index = i * (len(functions) + 1) + 1
        plot.subplot(subplot_rows, subplot_cols, subplot_index)
        plot.imshow(threshold.image)
        plot.axis('off')
        plot.title(f'Grayscale {title}')

        for j, f in enumerate(functions):
            result_image = threshold.apply(f)

            subplot_index = i * (len(functions) + 1) + 2 + j
            plot.subplot(subplot_rows, subplot_cols, subplot_index)
            plot.imshow(result_image)
            plot.axis('off')
            plot.title(f'Result {f.__name__}\n'
                       f'Amount: {threshold.particle_amount}\n'
                       f'Threshold value: {threshold.threshold_value: 08.4f}')

        print(f'Complete {title}')

    plot.savefig(get_artifact_path(f'threshold_{datetime.now().timestamp()}'),
                 bbox_inches='tight')


if __name__ == '__main__':
    from core.Utils import get_artifact_path
    from core import Dataset
    from core.Algorithm import Threshold
    import demo.config.config_threshold as config

    if len(sys.argv) >= 2 and len(sys.argv[1]) > 0:
        evaluate(sys.argv[1])
    else:
        evaluate()

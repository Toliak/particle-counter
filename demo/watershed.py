"""@package demo.watershed
Демонстрационный модуль для алгоритма водоразделов
"""
import sys
from datetime import datetime

import imageio
import matplotlib.pyplot as plot

import config.config_watershed as config

sys.path.append('..')


def save_iteration(index, subplot_rows, subplot_cols, watershed, result_image, title):
    """Сохранение результатов итерации
    @param index: Индекс изображения
    @param subplot_rows: Количество строк
    @param subplot_cols: Количество столбцов
    @param watershed: Объект обертки алгоритма водоразделов
    @param result_image: Результирующее изображение
    @param title: Заголовок изображения
    """
    subplot_index = index * subplot_cols + 1
    plot.subplot(subplot_rows, subplot_cols, subplot_index)
    plot.imshow(watershed.image)
    plot.axis('off')
    plot.title(f'Grayscale {title}')

    subplot_index = index * subplot_cols + 2
    plot.subplot(subplot_rows, subplot_cols, subplot_index)
    plot.imshow(result_image)
    plot.axis('off')
    plot.title(f'Result {title}\n'
               f'Amount: {watershed.particle_amount}')


def evaluate(image_path=None):
    """Демонстрация алгоритма водоразделов
    @param image_path: Пусть к изображению. Если None, то используется стандартный датасет
    """
    if image_path:
        dataset_list = [dict(image=imageio.imread(image_path),
                             title=image_path)]
        images_len = len(dataset_list)
    else:
        dataset_list = Dataset.get_full_dataset()
        images_len = len(dataset_list)

    subplot_rows = images_len  # Количество строк в визуализации
    subplot_cols = 2  # Количество столбцов в визуализации

    plot.figure(figsize=config.FIGSIZE)
    plot.subplots_adjust(**config.SUBPLOT_ADJUST)

    for i, data in enumerate(dataset_list):
        image, title = data['image'], data['title']

        # Выполнение алгоритма водораздела
        watershed = Watershed(image)
        result_image = watershed.apply()

        save_iteration(index=i,
                       subplot_rows=subplot_rows,
                       subplot_cols=subplot_cols,
                       watershed=watershed,
                       result_image=result_image,
                       title=title)

        print(f'Complete {title}')

    plot.savefig(get_artifact_path(f'watershed_{datetime.now().timestamp()}'),
                 bbox_inches='tight')


if __name__ == '__main__':
    from core import Dataset
    from core.Algorithm import Watershed
    from core.Utils import get_artifact_path

    ## @copydoc core.Algorithm.Watershed::MINIMAL_GRAY
    Watershed.MINIMAL_GRAY = config.WATERSHED_MINIMAL_GRAY

    ## @copydoc core.Algorithm.Watershed::MINIMAL_GRAY_MARKER
    Watershed.MINIMAL_GRAY_MARKER = config.WATERSHED_MINIMAL_GRAY_MARKER

    if len(sys.argv) >= 2:
        evaluate(sys.argv[1])
    else:
        evaluate()

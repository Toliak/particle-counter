"""@package Utils
Утилитарный функции
"""

import matplotlib.pyplot as plot
from skimage.color import rgb2gray


def visualize(image, label='', cmap='viridis', figsize=(8,8)):
    """Простая визуализация изображения

    @param image: Изображение
    @param label: Заголовок
    @param cmap: Цветовая гамма
    @param figsize: Размер результирующего изображения

    @return Визуализированное изображение
    """
    plot.figure(figsize=figsize)
    plot.axis('off')
    plot.imshow(image, cmap=cmap)
    plot.title(label)

    return plot.show()


def image_to_grayscale(image):
    """Преобразование 3-х канального изображение в 1-канальный с диапазоном серого [0, 255]

    @param image: Изображение

    @return Преобразованное изображения
    """
    result = rgb2gray(image)
    result *= (255.0 / result.max())  # rescale

    return result

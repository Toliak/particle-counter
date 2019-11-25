"""@package core.Utils
Утилитарный функции
"""
import os

import matplotlib.pyplot as plot
import numpy as np
from scipy.ndimage import label
from skimage.color import rgb2gray


def visualize(image, label='', cmap='viridis', figsize=(8, 8)):
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


def get_artifact_path(name):
    """Получение пути для сохранения артефакта. Создание
    @param name: Название артефакта
    @return Путь для сохранения
    """

    if not os.path.exists('../artifacts/'):
        os.makedirs('../artifacts/')

    path = f'../artifacts/{name}.png'
    print(f'New artifact: {path}')
    return path


def is_background(image: np.ndarray, max_gray, percent):
    """Является ли переданное изображение фоновым
    @param image: Исходное изображение
    @param max_gray: Предельное значение яркости фона
    @param percent: Минимальный процент пикселей фона
    @return True, если является, иначе - False
    """
    useless_pixels = (image == 0).sum()
    binary: np.ndarray = image <= max_gray

    percent_result = (binary.sum() - useless_pixels) / (binary.size - useless_pixels)
    return percent_result >= percent


def label_peak_amount(image, min_gray, min_size):
    """Тривиальный подсчет количества частиц на изображении
    @param image: Исходное изображение
    @param min_gray: Минимальная яркость для учета частицы
    @param min_size: Минимальный размер области частицы
    @return Изображение с пронумерованными частицами и количество частиц
    """
    binary = image > min_gray
    result, amount = label(binary)

    for i in range(1, amount + 1):
        label_only = result == i
        if label_only.sum() > min_size:
            continue

        result[label_only == 1] = 0

    return result, amount

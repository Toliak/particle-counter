"""@package Utils
Утилитарный функции
"""
import os

import matplotlib.pyplot as plot
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


def is_background(image):
    """Является ли переданное изображение фоновым
    @param image: Исходное изображение
    @return True, если является, иначе - False
    """
    PERCENT = 0.85
    MAX_GRAY = 0.2

    useless_pixels = (image == 0).sum()
    binary = image <= MAX_GRAY
    percent = (binary.sum() - useless_pixels) / (binary.size - useless_pixels)
    return percent >= PERCENT


def label_peak_amount(image):
    """Тривиальный подсчет количества частиц на изображении
    @param image: Исходное изображение
    @return Изображение с пронумерованными частицами и количество частиц
    """
    MIN_GRAY = 0.52
    MIN_SIZE = 35

    binary = image > MIN_GRAY
    result, amount = label(binary)

    for i in range(1, amount + 1):
        label_only = result == i
        if label_only.sum() > MIN_SIZE:
            continue

        result[label_only == 1] = 0

    return result, amount

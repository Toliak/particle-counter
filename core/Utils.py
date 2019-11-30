"""@package core.Utils
@brief Утилитарные функции
"""
import os

import numpy as np
from scipy.ndimage import label


def get_artifact_path(name):
    """Получение пути для сохранения артефакта. Side-эффект: Создание директории
    @param name: Название артефакта
    @return Путь для сохранения
    """

    if not os.path.exists('../artifacts/'):
        os.makedirs('../artifacts/')

    path = f'../artifacts/{name}.png'
    print(f'New artifact: {path}')
    return path


def is_background(image, max_gray, percent):
    """Является ли переданное изображение фоновым
    @param image: Исходное изображение
    @param max_gray: Предельное значение яркости фона
    @param percent: Минимальный процент пикселей фона
    @return True, если является, иначе - False
    """
    image: np.ndarray = image  # Remove pycharm warning

    useless_pixels = (image == 0).sum()
    binary: np.ndarray = image <= max_gray

    percent_result = (binary.sum() - useless_pixels) / (binary.size - useless_pixels)
    return bool(percent_result >= percent)


def label_peak_amount(image, min_gray, min_size):
    """Тривиальный подсчет количества частиц на изображении
    @param image: Исходное изображение
    @param min_gray: Минимальная яркость для учета частицы
    @param min_size: Минимальный размер области частицы
    @return Изображение с пронумерованными частицами и количество частиц
    """
    binary = image >= min_gray
    result, amount = label(binary)

    for i in range(1, amount + 1):
        label_only = result == i
        if label_only.sum() >= min_size:
            continue

        result[label_only == 1] = 0
        amount -= 1

    return result, amount

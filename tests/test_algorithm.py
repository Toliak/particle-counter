"""@package tests.test_algorithm
@brief Тесты для родительского класса для алгоритмов
"""

import numpy as np
import pytest


@pytest.fixture
def image():
    """Фикстура для серого RGB изображения
    @return RGB изображение, содержащее только оттенки серого. Диапазон цвета: [0, 1]
    """
    rgb_image = np.array([
        [[0, 0, 0],
         [25, 25, 25],
         [50, 50, 50]],
        [[75, 75, 75],
         [100, 100, 100],
         [125, 125, 125]],
        [[175, 175, 175],
         [200, 200, 200],
         [255, 255, 255]],
    ])

    return rgb_image / rgb_image.max()


@pytest.fixture
def algorithm(image):
    """Фикстура демонстрационного изображения
    @return Демонстрационное изображение
    """
    from Algorithm import Algorithm

    return Algorithm(image)


def test_algorithm_to_gray(algorithm, image):
    """Проверка работы метода to_gray
    """
    algorithm.image = image
    algorithm.to_gray()

    assert algorithm.image.shape == (3, 3)
    assert algorithm.image.max() == 1
    assert algorithm.image.min() == 0


def test_algorithm_remove_noise(algorithm, image):
    """Проверка работы метода remove_noise
    """
    algorithm.image = image
    algorithm.to_gray()
    algorithm.remove_noise()

    assert algorithm.image.shape == (3, 3)
    assert algorithm.image.max() == 175
    assert algorithm.image.min() == 75


def test_algorithm_apply_nothing(algorithm):
    """Проверка работы метода remove_noise
    """
    old_image = algorithm.image.copy()

    algorithm.apply(1, 2, 3, any_kwarg=1)  # Передача любых значений

    # Состояние не изменилось
    assert old_image.any() == algorithm.image.any()

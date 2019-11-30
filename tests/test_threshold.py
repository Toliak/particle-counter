"""@package tests.test_threshold
@brief Тесты для порогового алгоритма
"""
import sys

import imageio
import pytest
from skimage.filters import threshold_isodata, threshold_mean, threshold_triangle, threshold_otsu

sys.path.append('..')


@pytest.fixture
def demo_image():
    """Фикстура демонстрационного изображения
    @return Демонстрационное изображение
    """
    from core import Dataset

    return Dataset.load_by_path('multiple_gray.png')


def test_threshold_demo_image_availability(demo_image):
    """Проверка доступности демонстрационного изображения
    """
    assert demo_image is not None
    assert type(demo_image) == imageio.core.util.Array


## Значения для параметризованных параметров проверки порогового алгоритма
threshold_test_data = [
    ('multiple_gray.png', threshold_isodata, 9, 0),
    ('multiple_gray.png', threshold_mean, 12, 0),
    ('multiple_gray.png', threshold_triangle, 16, 0),
    ('multiple_gray.png', threshold_otsu, 9, 0),

    ('001_p.png', threshold_isodata, 8044, 50),
    ('001_p.png', threshold_mean, 7500, 300),
    ('001_p.png', threshold_otsu, 8044, 50),

    ('005_p.png', threshold_isodata, 870, 50),
    ('005_p.png', threshold_mean, 870, 100),
    ('005_p.png', threshold_triangle, 870, 250),
    ('005_p.png', threshold_otsu, 870, 50),

    ('006.jpeg', threshold_isodata, 732, 10),
    ('006.jpeg', threshold_mean, 630, 50),
    ('006.jpeg', threshold_triangle, 630, 50),
    ('006.jpeg', threshold_otsu, 732, 10),

    ('007_p.png', threshold_isodata, 510, 10),
    ('007_p.png', threshold_mean, 510, 40),
    ('007_p.png', threshold_otsu, 510, 10),

    ('009_p.png', threshold_isodata, 1000, 25),
    ('009_p.png', threshold_otsu, 1000, 25),

    ('014_p.png', threshold_isodata, 40, 6),
    ('014_p.png', threshold_otsu, 40, 6),
]


@pytest.mark.parametrize("name, function, expected_amount, epsilon", threshold_test_data)
def test_threshold_demo_image_threshold(name, function, expected_amount, epsilon):
    """Проверка определения количества точек пороговым алгоритмом

Параметры являются параметризованными

@param name: Название изображения
@param function: Пороговая функция
@param expected_amount: Ожидаемое значение
@param epsilon: Отрезок неопределенности
    """
    from core import Dataset
    from Algorithm import Threshold

    image = Dataset.load_by_path(name)

    threshold = Threshold(image)
    threshold.apply(function)

    assert type(threshold.particle_amount) == int
    assert expected_amount - epsilon // 2 <= threshold.particle_amount <= expected_amount + epsilon // 2

"""@package tests.watershed
@brief Тесты для алгоритма водоразделов
"""
import sys

import imageio
import pytest

sys.path.append('..')


@pytest.fixture
def demo_image():
    """Фикстура демонстрационного изображения
    @return Демонстрационное изображение
    """
    from core import Dataset

    return Dataset.load_by_path('multiple_gray.png')


def test_watershed_demo_image_availability(demo_image):
    """Проверка доступности демонстрационного изображения
    """
    assert demo_image is not None
    assert type(demo_image) == imageio.core.util.Array


## Значения для параметризованных параметров проверки порогового алгоритма
watershed_test_data = [
    ('multiple_gray.png', 7, 0),
    ('001_p.png', 8450, 100),
    ('005_p.png', 890, 10),
    ('006.jpeg', 650, 12),
    ('012_1_p.png', 1920, 20),
    ('014_p.png', 70, 4),
    ('016_p.png', 700, 20),
]

watershed_config = dict(minimal_gray=60,
                        minimal_gray_marker=140)


@pytest.mark.parametrize("name, expected_amount, epsilon", watershed_test_data)
def test_watershed_demo_image_watershed(name, expected_amount, epsilon):
    """Проверка определения количества точек пороговым алгоритмом

Параметры являются параметризованными

@param name: Название изображения
@param expected_amount: Ожидаемое значение
@param epsilon: Отрезок неопределенности
    """
    from core import Dataset
    from core.Algorithm import Watershed

    image = Dataset.load_by_path(name)

    watershed = Watershed(image, **watershed_config)
    watershed.apply()

    assert type(watershed.particle_amount) == int
    assert expected_amount - epsilon // 2 <= watershed.particle_amount <= expected_amount + epsilon // 2

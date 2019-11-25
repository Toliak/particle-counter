"""@package tests.test_threshold
@brief Тесты для порогового алгоритма
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


def test_threshold_demo_image_availability(demo_image):
    """Проверка доступности демонстрационного изображения
    """
    assert demo_image is not None
    assert type(demo_image) == imageio.core.util.Array

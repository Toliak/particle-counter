"""@package tests.test_threshold
Тесты для порогового алгоритма
"""
import imageio
import pytest


@pytest.fixture
def demo_image():
    """Фикстура демонстрационного изображения
    @return Демонстрационное изображение
    """
    import Dataset

    return Dataset.load_by_path('multiple_gray.png')


def test_threshold_demo_image_availability():
    """Проверка доступности демонстрационного изображения
    """
    assert demo_image is not None
    assert type(demo_image) == imageio.core.util.Array

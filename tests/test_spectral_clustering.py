"""@package tests.test_spectral_clustering
@brief Тесты для алгоритма спектральной кластеризации
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

    return Dataset.load_by_path('test_cluster.png')


def test_spectral_clustering_demo_image_availability(demo_image):
    """Проверка доступности демонстрационного изображения
    """
    assert demo_image is not None
    assert type(demo_image) == imageio.core.util.Array


class TestConfig:
    FIGSIZE = (15, 12)
    ITERATIONS = 3
    GRAPH_BETA = (15, 15, 15)
    GRAPH_EPS = (1e-6, 1e-6, 1e-6)
    N_CLUSTERS = (10, 5, 3)
    N_INIT = (2, 2, 2)
    LABELS = ('kmeans', 'kmeans', 'kmeans')
    RESULT_OUTPUT_SIZE = ((10, 10), (15, 30), (15, 30))
    FIRST_MAX_TRANSFORM_SIZE = 256
    RANDOM_STATE = 500
    BACKGROUND_MAX_GRAY = 0.2
    BACKGROUND_PERCENT = 0.85
    LABEL_PEAK_MIN_GRAY = 0.52
    LABEL_PEAK_MIN_SIZE = 35


def test_spectral_clustering_demo_image(demo_image):
    """Проверка доступности демонстрационного изображения
    """

    from demo.spectral_clustering import evaluate

    result = evaluate(TestConfig)

    assert result == 10

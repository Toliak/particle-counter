"""@package tests.test_dataset
@brief Тесты для датасета
"""
import sys

import imageio
import pytest

sys.path.append('..')


def test_dataset_load_by_path_error():
    """Проверка метода
    """
    from core.Dataset import load_by_path

    with pytest.raises(Exception):
        load_by_path('__exactly_not_existing_file__')


def test_dataset_get_full_dataset():
    """Проверка доступности демонстрационного изображения
    """
    from core.Dataset import get_full_dataset

    dataset = get_full_dataset()

    assert type(dataset) == list
    assert len(dataset) > 0

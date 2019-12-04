"""@package tests.test_utils
@brief Тесты для утилитарных функций
"""
import sys

import numpy as np

sys.path.append('..')


def test_utils_get_artifact_path():
    """Проверка работоспособности функции выдачи пути артефакта
    """
    from core.Utils import get_artifact_path

    path = get_artifact_path('custom_name')
    assert 'artifact' in path
    assert 'custom_name' in path


def test_utils_is_background():
    """Проверка функции определения фона
    """
    from core.Utils import is_background

    image = np.array([
        [0.1, 0.1, 0.0],
        [0.1, 0.2, 0.0],
        [0.0, 0.1, 0.0]
    ])

    assert is_background(image, 0.2, 0.5) is True
    assert is_background(image, 0.2, 1) is True

    assert is_background(image, 0.1, 0.5) is True

    assert is_background(image, 0.0, 0.5) is False


def test_utils_label_peak_amount():
    """Проверка функции базового подсчета количества частиц
    """
    from core.Utils import label_peak_amount

    image = np.array([
        [0.1, 0.2, 0.0],
        [0.2, 0.1, 0.0],
        [0.0, 0.2, 0.0]
    ])

    assert label_peak_amount(image, 0.2, 1)[1] == 3
    assert label_peak_amount(image, 0.2, 2)[1] == 0

    assert label_peak_amount(image, 0.1, 1)[1] == 1
    assert label_peak_amount(image, 0.1, 4)[1] == 1
    assert label_peak_amount(image, 0.1, 8)[1] == 0

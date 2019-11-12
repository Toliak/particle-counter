"""@package Threshold
Реализация порогового алгоритма
"""

from scipy.ndimage import label
from skimage import color
from skimage.filters import rank
from skimage.morphology import disk


class Threshold:
    """Реализация порогового алгоритма
    @var image: Целевое изображение
    @var particle_amount: Количество частиц
    @var threshold_value: Пороговое число
    """

    def __init__(self, image):
        """Инициализация порогового алгоритма

Копирует переданное изображение

@param image: Изображение для обработки
        """
        self.image = image.copy()

        self.to_gray()
        self.remove_noise()

        self.particle_amount = None
        self.threshold_value = None

    def to_gray(self):
        """Преобразование изображения в оттенки серого
        """
        self.image = color.rgb2gray(self.image)

    def remove_noise(self, level=2):
        """Медианный алгоритм для уменьшения шумов
        @param level: Радиус диска (ядра)
        """
        self.image = rank.median(self.image, disk(2))

    def apply_threshold(self, function):
        """Медианный алгоритм для уменьшения шумов
        @param function: Функция определения порогового значения
        @return Результирующее изображение
        """

        self.threshold_value = function(self.image)
        binary = self.image > self.threshold_value

        result_image, self.particle_amount = label(binary)

        return result_image



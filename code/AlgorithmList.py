"""@package AlgorithmList
Родительский класс для реализаций алгоритмов сегментации (со списком изображений)
"""

from skimage import color
from skimage.filters import rank
from skimage.morphology import disk


class AlgorithmList:
    """Родительский класс для реализаций алгоритмов сегментации (со списком изображений)
    """

    ## Целевые изображения
    image_list = None

    def __init__(self, image_list):
        """Инициализация порогового алгоритма

Копирует переданные изображение

@param image_list: Изображения для обработки
        """
        self.image_list = [i.copy() for i in image_list]

        self.to_gray()
        self.remove_noise()

    def to_gray(self):
        """Преобразование изображений в оттенки серого
        """
        for i, image in enumerate(self.image_list):
            self.image_list[i] = color.rgb2gray(image)

    def remove_noise(self, level=2):
        """Медианный алгоритм для уменьшения шумов
        @param level: Радиус диска (ядра)
        """
        for i, image in enumerate(self.image_list):
            self.image_list[i] = rank.median(image, disk(2))
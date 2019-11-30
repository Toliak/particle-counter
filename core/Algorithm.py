"""@package core.Algorithm
@brief Алгоритмы сегментации, работающие с одним изображением
"""
from scipy.ndimage import distance_transform_edt
from scipy.ndimage import label
from skimage import color, img_as_ubyte
from skimage.filters import rank
from skimage.morphology import disk, watershed


class Algorithm:
    """Родительский класс для реализаций алгоритмов сегментации
    """

    ## Целевое изображение
    image = None

    ## Количество частиц
    particle_amount = None

    def __init__(self, image):
        """Инициализация алгоритма

Копирует переданное изображение

@param image: Изображение для обработки
        """
        self.image = image.copy()

        self.to_gray()
        self.remove_noise()

    def to_gray(self):
        """Преобразование изображения в оттенки серого
        """
        self.image = color.rgb2gray(self.image)

    def remove_noise(self, level=2):
        """Медианный алгоритм для уменьшения шумов
        @param level: Радиус диска (ядра)
        """
        self.image = rank.median(img_as_ubyte(self.image), disk(level))

    def apply(self, *args, **kwargs):
        """Реализация алгоритма
        """
        pass


class Threshold(Algorithm):
    """Реализация порогового алгоритма
    """

    ## Пороговое значение
    threshold_value = None

    ## Количество частиц
    particle_amount = None

    def __init__(self, image):
        """
        @copydoc Algorithm::\_\_init\_\_()
        """
        super().__init__(image)

    def apply(self, function):
        """Реализация порогового алгоритма
        @param function: Функция определения порогового значения
        @return Результирующее изображение
        """

        self.threshold_value = function(self.image)
        binary = self.image > self.threshold_value

        result_image, self.particle_amount = label(binary)

        return result_image


class Watershed(Algorithm):
    """Реализация алгоритма водоразделов
    """

    ## Минимальная яркость для построения карты расстояний
    minimal_gray = None

    ## Минимальная яркость для маркировки
    minimal_gray_marker = None

    ## Количество частиц
    particle_amount = None

    def __init__(self, image, minimal_gray=60, minimal_gray_marker=150):
        """
        @copydoc Algorithm::\_\_init\_\_()
        @param minimal_gray: Минимальная яркость для построения карты расстояний
        @param minimal_gray_marker: Минимальная яркость для маркировки
        """
        super().__init__(image)

        self.minimal_gray = minimal_gray
        self.minimal_gray_marker = minimal_gray_marker

    def apply(self):
        """Реализация алгоритма водоразделов
        @return Результирующее изображение
        """

        distance = distance_transform_edt(self.image > self.minimal_gray)
        markers, self.particle_amount = label(self.image > self.minimal_gray_marker)
        watershed_result = watershed(-distance,
                                     markers,
                                     mask=self.image > self.minimal_gray)

        return watershed_result

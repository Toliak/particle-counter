"""@package core.Dataset
Содержит изображения частиц
"""

import os
import urllib.request

import imageio


def load_by_path(path):
    """Загрузка изображения из интернет-хранилища

    @param path: Относительный путь к изображению внутри хранилища

    @return Полученное изображение

    @warning Кэширует изображения в директории data
    """
    url = f'https://s3.toliak.ru/course-project-2019/images/{path}'
    path = f'../data/{path}'

    if not os.path.exists('../data/'):
        os.makedirs('../data/')
    if not os.path.isfile(f'../data/{path}'):
        urllib.request.urlretrieve(url, path)

    return imageio.imread(path)


def hard():
    """"""
    return load_by_path('001_p.png')


def large_1x():
    """"""
    return load_by_path('002_p.png')


def large_2x():
    """"""
    return load_by_path('003_p.png')


def large_4x():
    """"""
    return load_by_path('004_p.png')


def flat():
    """"""
    return load_by_path('005_p.png')


def easy():
    """"""
    return load_by_path('006.jpeg')


def easy_large():
    """"""
    return load_by_path('007_p.png')


def light():
    """"""
    return load_by_path('009_p.png')


def gray_background():
    """"""
    return load_by_path('010_p.png')


def easy_spheres():
    """"""
    return load_by_path('011_p.png')


def medium():
    """"""
    return load_by_path('012_1_p.png')


def low_amount():
    """"""
    return load_by_path('012_2_p.png')


def easy_medium():
    """"""
    return load_by_path('013_p.png')


def low_amount_noise():
    """"""
    return load_by_path('014_p.png')


def light_many():
    """"""
    return load_by_path('015_p.png')


def easy_medium_many():
    """"""
    return load_by_path('016_p.png')


def get_full_dataset():
    """Загрузка всех изображений из датасета

    @return Список всех изображений
    """
    return [
        dict(image=hard(),
             title='hard'),
        dict(image=large_1x(),
             title='large_1x'),
        dict(image=large_2x(),
             title='large_2x'),
        dict(image=large_4x(),
             title='large_4x'),
        dict(image=flat(),
             title='flat'),
        dict(image=easy(),
             title='easy'),
        dict(image=easy_large(),
             title='easy_large'),
        dict(image=light(),
             title='light'),
        dict(image=gray_background(),
             title='gray_background'),
        dict(image=easy_spheres(),
             title='easy_spheres'),
        dict(image=medium(),
             title='medium'),
        dict(image=low_amount(),
             title='low_amount'),
        dict(image=easy_medium(),
             title='easy_medium'),
        dict(image=low_amount_noise(),
             title='low_amount_noise'),
        dict(image=light_many(),
             title='light_many'),
        dict(image=easy_medium_many(),
             title='easy_medium_many'),
    ]

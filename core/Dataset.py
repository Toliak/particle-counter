"""@package core.Dataset
@brief Содержит изображения частиц
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
             title='1'),
        dict(image=large_1x(),
             title='2'),
        dict(image=large_2x(),
             title='3'),
        dict(image=large_4x(),
             title='4'),
        dict(image=flat(),
             title='Au particles on SEM'),
        dict(image=easy(),
             title='Au nanoparticles on SEM'),
        dict(image=easy_large(),
             title='Au cluster on HPOG'),
        dict(image=light(),
             title='Au particles on FEG'),
        dict(image=gray_background(),
             title='Atomized silver powder on BEM'),
        dict(image=easy_spheres(),
             title='Atomized silver powder 4x on SEM'),
        dict(image=medium(),
             title='Carbon adhesive on SEM'),
        dict(image=low_amount(),
             title='Carbon adhesive\non vacuum dispersion system'),
        dict(image=easy_medium(),
             title='Atomized silver powder 1x on SEM'),
        dict(image=low_amount_noise(),
             title='Carbenoxolone\n(low expression level) on SEM'),
        dict(image=light_many(),
             title='Carbenoxolone on SEM'),
        dict(image=easy_medium_many(),
             title='20MnCr5 powder on SEM'),
    ]

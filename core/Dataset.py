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


def get_full_dataset():
    """Загрузка всех изображений из датасета

    @return Список всех изображений
    """
    return [
        dict(image=load_by_path('001_p.png'),
             title='1'),
        dict(image=load_by_path('001_p.png'),
             title='2'),
        dict(image=load_by_path('003_p.png'),
             title='3'),
        dict(image=load_by_path('004_p.png'),
             title='4'),
        dict(image=load_by_path('005_p.png'),
             title='Au particles on SEM'),
        dict(image=load_by_path('006.jpeg'),
             title='Au nanoparticles on SEM'),
        dict(image=load_by_path('007_p.png'),
             title='Au cluster on HPOG'),
        dict(image=load_by_path('009_p.png'),
             title='Au particles on FEG'),
        dict(image=load_by_path('010_p.png'),
             title='Atomized silver powder on BEM'),
        dict(image=load_by_path('011_p.png'),
             title='Atomized silver powder 4x on SEM'),
        dict(image=load_by_path('012_1_p.png'),
             title='Carbon adhesive on SEM'),
        dict(image=load_by_path('012_2_p.png'),
             title='Carbon adhesive\non vacuum dispersion system'),
        dict(image=load_by_path('013_p.png'),
             title='Atomized silver powder 1x on SEM'),
        dict(image=load_by_path('014_p.png'),
             title='Carbenoxolone\n(low expression level) on SEM'),
        dict(image=load_by_path('015_p.png'),
             title='Carbenoxolone on SEM'),
        dict(image=load_by_path('016_p.png'),
             title='20MnCr5 powder on SEM'),
    ]

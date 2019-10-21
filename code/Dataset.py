import os
import urllib.request

import imageio


def load_by_path(path):
    url = f'https://s3.toliak.ru/course-project-2019/images/{path}'
    path = f'../data/{path}'

    if not os.path.exists('../data/'):
        os.makedirs('../data/')
    if not os.path.isfile(f'../data/{path}'):
        urllib.request.urlretrieve(url, path)

    return imageio.imread(path)


def hard():
    return load_by_path('001_p.png')


def large_1x():
    return load_by_path('002_p.png')


def large_2x():
    return load_by_path('003_p.png')


def large_4x():
    return load_by_path('004_p.png')


def flat():
    return load_by_path('005_p.png')


def easy():
    return load_by_path('006.jpeg')


def easy_large():
    return load_by_path('007_p.png')


def light():
    return load_by_path('009_p.png')


def gray_background():
    return load_by_path('010_p.png')


def easy_spheres():
    return load_by_path('011_p.png')


def get_full_dataset() -> list:
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
    ]

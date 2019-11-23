# Определение количества частиц на изображении

## Задача


## Файлы

[Литература](https://s3.toliak.ru/minio/course-project-2019/literature/)

## Сборка

Перед запуском необходимо установить зависимости.
Используется настройщик виртуальной среды ``pipenv``.

Используемая версия Python: 3.7

```bash
pip install -U pip pipenv
pipenv install
```

## Запуск

```bash
APP_NAME=threshold|watershed|spectral_clustering
python3 demo/$APP_NAME.py
```

## Запуск с использованием Docker

```bash
docker build . --tag particle_bootstrap
docker run --rm -it -v $(pwd):/opt/builder/ particle_bootstrap
```

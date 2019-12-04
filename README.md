[![Build Status](https://travis-ci.com/Toliak/particle-counter.svg?branch=master)](https://travis-ci.com/Toliak/particle-counter)
[![pipeline status](https://gitlab.toliak.ru/Toliak/particle-counter/badges/master/pipeline.svg)](https://gitlab.toliak.ru/Toliak/particle-counter/commits/master)
![Code size](https://img.shields.io/github/languages/code-size/Toliak/particle-counter.svg)
![GitHub Repo size](https://img.shields.io/github/repo-size/Toliak/particle-counter.svg)

# Курсовой проект

Подсчет частиц на изображениях электронных микроскопов

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
APP_NAME=threshold|watershed|spectral_clustering
BRANCH=latest|dev
./scripts/docker.sh $BRANCH python $APP_NAME.py
```

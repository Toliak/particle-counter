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

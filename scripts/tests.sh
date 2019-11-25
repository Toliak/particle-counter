#! /bin/sh

set -ex

pip install pytest pytest-cov

pytest --cov=core .
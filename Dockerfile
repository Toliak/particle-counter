FROM python:3.7-slim-buster

COPY Pipfile /tmp/Pipfile

ENV PACKAGES="gcc \
              build-essential \
              python3-dev"

RUN set -ex && \
    apt-get update -y && \
    apt-get install -y $PACKAGES && \
    pip install -U pip \
                   pipenv && \
    cd /tmp/ && \
    pipenv install --deploy --system --skip-lock && \
    apt-get remove -y $PACKAGES && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt

VOLUME /opt/builder
WORKDIR /opt/builder

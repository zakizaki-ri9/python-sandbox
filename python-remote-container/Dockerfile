FROM python:3.9-rc-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

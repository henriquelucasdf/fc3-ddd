FROM python:3.8.15-slim-buster

COPY requirements.txt .

RUN apt update -y\
    && apt-get install git -y\
    && pip install -r requirements.txt

ENV PYTHONPATH "/workspaces/fc3-ddd/"

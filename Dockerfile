FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /myproject
WORKDIR /myproject

EXPOSE 8000

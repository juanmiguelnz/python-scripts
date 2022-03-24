FROM python:3

RUN apt update && apt upgrade

WORKDIR /scripts

COPY . .
FROM python:3

RUN apt update && apt upgrade -y

WORKDIR /scripts

COPY . .
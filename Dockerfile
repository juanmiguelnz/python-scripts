FROM ubuntu

RUN apt update && apt upgrade

WORKDIR /scripts

COPY . .
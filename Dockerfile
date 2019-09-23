# Getting base image
FROM continuumio/anaconda3

RUN apt-get update \
    && apt-get -y install mysql-client

COPY ./project /root/home/portal

ENTRYPOINT ["python", "/root/home/portal/main.py"]

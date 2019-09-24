# Getting base image
FROM continuumio/anaconda3

RUN apt-get update \
    && apt-get -y install mysql-client \
    && pip install --upgrade pip \
    && pip install pymysql

COPY ./portal /root/home/portal

ENTRYPOINT ["python", "/root/home/portal/main.py"]

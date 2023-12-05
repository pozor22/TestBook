FROM python:3.10

COPY requirements.txt /temp/requirements.txt
COPY booktest /booktest
WORKDIR /booktest
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user

USER service-user
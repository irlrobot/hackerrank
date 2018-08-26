FROM python:3.6-alpine3.8

COPY ./30_days_of_code /src/30_days_of_code
COPY ./algorithms /src/algorithms

WORKDIR /src

ENTRYPOINT python
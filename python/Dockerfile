FROM python:3.6-alpine3.8
LABEL maintainer="josh@userdel.com"

COPY . /src/

WORKDIR /src

RUN adduser --disabled-password --gecos "" josh

USER josh

ENTRYPOINT ["python"]
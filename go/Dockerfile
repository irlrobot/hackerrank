FROM golang:1.11.1-alpine3.8

COPY . /src/

WORKDIR /src

RUN adduser --disabled-password --gecos "" josh

USER josh

ENTRYPOINT ["go"]
FROM ubuntu:latest
LABEL authors="wel"

ENTRYPOINT ["top", "-b"]
FROM python:latest

WORKDIR /app
COPY . /app/

RUN set -ex ;\
    pip3 install -r requirements.txt &&\
    python3 tests.py


COPY ./docker/app/docker-entrypoint.sh /


ENTRYPOINT ["/docker-entrypoint.sh"]
STOPSIGNAL SIGQUIT

EXPOSE 5000/tcp
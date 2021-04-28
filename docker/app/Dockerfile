FROM python:latest

WORKDIR /app
COPY ./flask /app/

RUN set -ex ;\
    pip3 install -r requirements.txt &&\
    FLASK_ENV=testing python3 tests.py


COPY ./docker/app/docker-entrypoint.sh /
#RUN set -ex ;\
#    chmod +x /docker-entrypoint.sh


ENTRYPOINT ["/docker-entrypoint.sh"]
STOPSIGNAL SIGQUIT

EXPOSE 5000/tcp
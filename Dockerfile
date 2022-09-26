FROM python:3

RUN apt-get update && \
    apt-get -y install zip && \
    apt-get -y install libaio1

RUN mkdir /oracle

ADD ./oracle /oracle

WORKDIR /oracle
RUN unzip instantclient-basic-linux.x64-19.13.0.0.0dbru.zip
RUN unzip instantclient-sdk-linux.x64-19.13.0.0.0dbru.zip
RUN unzip instantclient-sqlplus-linux.x64-19.13.0.0.0dbru.zip

ENV PATH=/oracle/instantclient_19_13:$PATH
ENV ORACLE_HOME=/oracle
ENV TNS_ADMIN=$ORACLE_HOME
ENV NLS_LANG=JAPANESE_JAPAN.AL32UTF8
ENV LD_LIBRARY_PATH=/oracle/instantclient_19_13:$LD_LIBRARY_PATH

RUN mkdir /app

ADD ./app /app

RUN pip install cx_Oracle
RUN pip install docopt

ENV PYTHONPATH "/app:$PYTHONPATH"

WORKDIR /app
FROM python:3.8

WORKDIR /home

ENV TELEGRAM_API_TOKEN="1059542923:AAGbXtxMxHvcd9p8Y_7NlkM4Wulm47FL8c0"
ENV TELEGRAM_PROXI_URL="http://209.250.248.123:3128"

RUN pip3 install -U pip aiogram pytz && apt-get update && apt-get install sqlite3

COPY *.py ./
COPY createdb.sql ./

ENTRYPOINT ["python", "server.py"]

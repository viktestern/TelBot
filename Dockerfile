FROM python:3.8

WORKDIR /home

ENV TELEGRAM_API_TOKEN="1059542923:AAGbXtxMxHvcd9p8Y_7NlkM4Wulm47FL8c0"
ENV TELEGRAM_ACCESS_ID="292926613"
#ENV TELEGRAM_PROXY_URL=""
#ENV TELEGRAM_PROXY_LOGIN=""
#ENV TELEGRAM_PROXY_PASSWORD=""

RUN pip install -U pip aiogram pytz && apt-get update && apt-get install sqlite3
COPY *.py ./
COPY createdb.sql ./

ENTRYPOINT ["python", "server.py"]


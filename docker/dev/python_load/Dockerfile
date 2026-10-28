FROM python:3.8-slim

RUN apt-get update -y && \
    apt-get install -y libpq-dev gcc

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

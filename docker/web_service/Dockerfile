from python:3.7

WORKDIR /app
COPY . /app
RUN mv /app/env_example /app/.env

RUN pip install -r requirements.txt

EXPOSE 8000

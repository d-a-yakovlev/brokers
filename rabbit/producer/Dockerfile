FROM python:3.7

RUN pip install pika

ENV PYTHONUNBUFFERED=1

WORKDIR /home/da/prog/broker/rabbit/producer

COPY producer.py .

CMD [ "python", "producer.py" ]

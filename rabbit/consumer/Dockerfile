FROM python:3.7

RUN pip install pika

ENV PYTHONUNBUFFERED=1

WORKDIR /home/da/prog/broker/rabbit/consumer

COPY consumer.py .

CMD [ "python", "consumer.py" ]

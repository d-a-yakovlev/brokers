FROM python:3.7

RUN pip install kafka-python

ENV PYTHONUNBUFFERED=1

WORKDIR /home/da/prog/broker/kafka/producer

COPY producer.py .

CMD [ "python", "producer.py" ]

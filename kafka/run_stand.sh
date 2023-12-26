#!/bin/bash

docker-compose up -d

python3 -m venv venv

venv/bin/python3 -m pip install kafka-python

sleep 5

venv/bin/python3 producer/producer.py
venv/bin/python3 consumer/consumer.py

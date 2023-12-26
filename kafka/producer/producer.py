import os
import time
import random
from kafka import KafkaProducer

KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
KAFKA_TOPIC_TEST = os.environ.get("KAFKA_TOPIC_TEST", "testing")
KAFKA_API_VERSION = os.environ.get("KAFKA_API_VERSION", "7.5.2")


def main(producer):
    messages = []
    base_message = "Hello, is it me you're looking for?"
    keywords = ['main', 'retry', 'error']
    for keyword in keywords:
        messages.append(keyword + " " + base_message)

    for message in messages:
        producer.send(
            KAFKA_TOPIC_TEST,
            message.encode()
        )
        print(f"* [Produced] {message}")

    producer.flush()


if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
        api_version=KAFKA_API_VERSION,
    )
    main(producer)


import pika
import os
import time

amqp_url = os.environ['AMQP_URL']
exchanger_name = os.environ['EXCHANGER_NAME']
publications_count = int(os.environ['PUBLICATIONS_COUNT'])

def main():
    url_params = pika.URLParameters(amqp_url)

    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()
    message = "Hello, is it me you're looking for?"


    channel.exchange_declare(
        exchange=exchanger_name,
        exchange_type='fanout',
        durable=True
    )

    time.sleep(3) # sure, that consumers ups

    for i in range(publications_count):
        message_i = f"({i}) " + message
        channel.basic_publish(
            exchange=exchanger_name,
            routing_key='',
            body=message_i,
            properties=pika.BasicProperties(delivery_mode=2)
        )
        print(f'* [Produced] "{message_i}"')


    channel.close()
    connection.close()


if __name__ == "__main__":
    main()


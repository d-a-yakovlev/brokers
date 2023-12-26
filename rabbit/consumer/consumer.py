import pika
import time
import os

amqp_url = os.environ['AMQP_URL']
exchanger_name = os.environ['EXCHANGER_NAME']


def main():
    url_params = pika.URLParameters(amqp_url)

    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()

    channel.exchange_declare(
        exchange=exchanger_name,
        exchange_type='fanout',
        durable=True
    )


    result = channel.queue_declare(queue='', exclusive=True, durable=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange=exchanger_name, queue=queue_name)

    print(f"* [Waiting] for exchanger:'{exchanger_name}'")

    def callback(channel, method, properties, body):
        time.sleep(2)
        print(f'* [Consumed] "{body.decode()}"')
        channel.basic_ack(delivery_tag=method.delivery_tag)


    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback
    )

    channel.start_consuming()


if __name__ == "__main__":
    main()


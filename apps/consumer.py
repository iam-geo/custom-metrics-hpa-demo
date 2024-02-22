import pika
import time

from apps.config import config


def callback(ch, method, properties, body):
    print(f"Received {body}")
    time.sleep(config.consumer_delay_sec)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consumer():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=config.rabbitmq_server_name, port=config.rabbitmq_server_port
        )
    )
    channel = connection.channel()

    channel.queue_declare(queue=config.rabbitmq_queue_name)
    channel.basic_consume(
        queue=config.rabbitmq_queue_name, on_message_callback=callback
    )

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

    connection.close()

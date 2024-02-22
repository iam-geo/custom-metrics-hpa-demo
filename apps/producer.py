import pika
import sys
import time

from apps.config import config


def producer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=config.rabbitmq_server_name,
        port=config.rabbitmq_server_port))

    channel = connection.channel()
    channel.queue_declare(queue=config.rabbitmq_queue_name)

    # hard-coded max range for performance reasons
    for i in range(1200):
        channel.basic_publish(
            exchange='',
            routing_key=config.rabbitmq_queue_name,
            body='this is a message')

        print(" [*] Sent message to queue")
        time.sleep(config.producer_delay_sec)

    connection.close()
    sys.exit(0)

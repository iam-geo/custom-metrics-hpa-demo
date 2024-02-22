import pika
import time

from apps.config import config


def producer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=config.rabbitmq_server_name,
        port=config.rabbitmq_server_port))
    channel = connection.channel()

    channel.queue_declare(queue=config.rabbitmq_queue_name)

    # hard-coded max range of 1200 to not kill my laptop
    for i in range(1200):
        channel.basic_publish(
            exchange='',
            routing_key=config.rabbitmq_queue_name,
            body=f'Message {i} of 1200')

        print(f"Sent {i} of 1200 message to queue. Next message in {config.producer_delay_sec}s")

        # simulated delay
        time.sleep(config.producer_delay_sec)

    connection.close()
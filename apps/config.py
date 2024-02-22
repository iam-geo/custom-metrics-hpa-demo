import os

from dataclasses import dataclass


@dataclass
class Config:
    consumer_delay_sec: int
    producer_delay_sec: int
    rabbitmq_server_name: str
    rabbitmq_server_port: int
    rabbitmq_queue_name: str


config = Config(
    consumer_delay_sec=int(os.environ.get("CONSUMER_DELAY_SECONDS", 5)),
    producer_delay_sec=int(os.environ.get("PRODUCER_DELAY_SECONDS", 1)),
    rabbitmq_server_name=os.environ["RABBITMQ_SERVER_NAME"],
    rabbitmq_server_port=int(os.environ["RABBITMQ_SERVER_PORT"]),
    rabbitmq_queue_name=os.environ["RABBITMQ_QUEUE_NAME"],
)

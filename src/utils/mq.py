import pika
import json


def send_to_rabbitmq(message: dict):
    credentials = pika.PlainCredentials("user", "password")
    parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue="data_queue")
    channel.basic_publish(
        exchange="", routing_key="data_queue", body=json.dumps(message)
    )
    connection.close()

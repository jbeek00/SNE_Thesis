# Written with assistance of generative AI and online community forums.

import pika
import json

# RabbitMQ configuration
rabbitmq_host = ""  # Middleware server IP
exchange_name = "my_exchange_1"  # Name of the exchange to consume from (should match producer exchange)
routing_key = "key1.topic1"

# Credentials (as specified in message generator script and rabbit config)
credentials = pika.PlainCredentials('', '')

# Establish connection to RabbitMQ server
connection_parameters = pika.ConnectionParameters(host=rabbitmq_host, credentials=credentials)
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


def process_message(message):
    try:
        # Decode the JSON-encoded message body
        data = json.loads(message.body)

        # Print the message data only when a message is received
        print(f"Received message data: {data}")

    except (json.JSONDecodeError) as e:
        # Handle potential errors (message format might be different)
        print(f"Error: Message format not recognized ({e})")


def on_message_received(ch, method, properties, body):
    try:
        # Decode the JSON-encoded message body directly from the argument
        data = json.loads(body)
        # Print the message data only when a message is received
        print(f"Received message data: {data}")

    except (json.JSONDecodeError) as e:
        # Handle potential errors (message format might be different)
        print(f"Error: Message format not recognized ({e})")
    # Acknowledge the message to commit consumption progress
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Declare consumption (optional, especially if the queue doesn't exist yet)
channel.queue_declare(queue="queue_1_1", durable=True)

# Consume messages from the exchange with the specified routing key
channel.basic_consume(queue="queue_1_1",  # Specify the queue name
                      auto_ack=False,  # Manual acknowledgment
                      on_message_callback=on_message_received)

# Start consuming (enter the loop to wait for messages)
print("Waiting for messages...")
channel.start_consuming()

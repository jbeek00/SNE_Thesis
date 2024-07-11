# Written with assistance of generative AI and online community forums.

from kafka import KafkaConsumer
import json

# Kafka configuration (replace with your details)
bootstrap_servers = "IP HERE:9092"  # Middleware server IP here
topic_name = "Topic2"  # Datastream selection

consumer = KafkaConsumer(topic_name, group_id="my-group", bootstrap_servers=bootstrap_servers)

while True:
  # Check for message (blocking call)
  message = consumer.poll(timeout_ms=500)

  # Handle the case where no message is received
  if message is None:
    print("Awaiting messages (Sub rate > Pub rate)")
    continue  # Continue to the next loop iteration

  # Assuming messages are already JSON-encoded dictionaries (no decoding needed)
  try:
    # Access the message data directly (no decoding needed)
    data = message  # Entire message is the data (if it's a dictionary)
    # Print the message data only when a message is received
    print(f"Received message data: {data}")

  except (AttributeError, json.JSONDecodeError) as e:
    # Handle potential errors (message format might be different)
    print(f"Error: Message format not recognized ({e})")
    continue  # Skip processing this message

  # Acknowledge the message to commit consumption progress
  consumer.commit()

consumer.close()

# Written with assistance of generative AI and online community forums.

from pulsar import Client
import json

client = Client(service_url="pulsar:// IP HERE :6650") # Add Middleware server IP

consumer = client.subscribe("persistent://public/default/Topic 2", subscription_name="latency-subscription")

while True:
  msg = consumer.receive()
  try:
    # Assuming your messages are JSON-encoded, decode them here
    data = json.loads(msg.data().decode('utf-8'))

    # Get the "data" dictionary or an empty one if missing
    data_dict = data.get("data", {})

    # Iterate over "data" dictionary (if it exists)
    for inner_key, inner_value in data_dict.items():
      print(f"{inner_key}: {inner_value}")

      # Check for potentially missing keys within "data"
      if inner_key == "enemy_type":
        print(f"enemy_type: {inner_value}")  # Print "enemy_type" if it exists
      elif inner_key == "weapon_type":
        print(f"weapon_type: {inner_value}")  # Print "weapon_type" if it exists

    # Show message
    print(f"Received message data: {data}")

  except Exception as e:
    print(f"Error processing message: {e}")
  finally:
    consumer.acknowledge(msg)

client.close()

# Written with assistance of generative AI and online community forums.

import pika
import random
import string
import json
from pika import ConnectionParameters, BasicProperties

def generate_entity_id(entity_type):
  # Generate random alphanumeric string for entity_id with prefix based on type
  prefix_map = {
    "soldier": "soldier_",
    "aircraft": "aircraft_",
    "tank": "tank_"
  }
  return prefix_map[entity_type] + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


def generate_entity_type():
  # Define list of entity types
  entity_types = ["soldier", "aircraft", "tank"]
  return random.choice(entity_types)


def generate_message():
  entity_type = generate_entity_type()
  entity_id = generate_entity_id(entity_type)

  # Entity types and properties in a dictionary fashion
  event_type_map = {
    "soldier": ["moved", "fired_weapon", "detected", "destroyed", "repairing"],
    "aircraft": ["moved", "fired_weapon", "detected", "destroyed"],
    "tank": ["moved", "fired_weapon", "detected", "destroyed"]
  }
  event_type = random.choice(event_type_map[entity_type])

  data = None
  if event_type == "moved":
    data = {"x": random.randint(0, 100), "y": random.randint(0, 100)}
  elif event_type == "fired_weapon":
    # data corresponding to the specific entity properties
    if entity_type == "aircraft":
      data = {"weapon_type": random.choice(["missile", "turret", "atom_bomb"])}
    elif entity_type == "tank":
      data = {"weapon_type": "cannon"}
    elif entity_type == "soldier":
      data = {"weapon_type": random.choice(["rifle", "rifle", "bazooka", "pistol"])}
  elif event_type == "detected":
    data = {"enemy_type": random.choice(["soldier", "aircraft", "tank"])}
  elif event_type == "destroyed":
    data = None 
  elif event_type == "repairing":
    data = {"repair_progress": random.randint(0, 100)}  # Repair progression as %

  # This portion adds additional data to create a heavier message size
  additional_data = {}
  for _ in range(1000):  # 1000 loops of adding single 32-bit data units
    additional_data["data_field_" + str(_)] = random.getrandbits(32) 

  message = {
    "entity_id": entity_id,
    "entity_type": entity_type,
    "event_type": event_type,
    "data": data,
    "additional_data": additional_data
  }
  return message

# ---- RabbitMQ Configuration:

rabbitmq_host = ""  # Middleware server IP with brokers here
exchange_name = "my_exchange_1"  # Exchange here, for example: 'my_exchange_1'
routing_key = "key1.topic1"

# Establish connection to RabbitMQ server
connection_parameters = ConnectionParameters(host=rabbitmq_host, port=5672, credentials=pika.PlainCredentials('', ''))  # Access credentials ('Username', 'Password')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# Define properties for persistent messages (optional)
message_properties = BasicProperties(delivery_mode=2)  # Set delivery mode to 2 for persistence

# Continuously generate and publish messages
while True:
  message = generate_message()
  json_message = json.dumps(message).encode('utf-8')  # Encode for sending

  # Publish message to exchange with optional routing key
  channel.basic_publish(
      exchange=exchange_name,
      routing_key=routing_key,
      body=json_message
    )

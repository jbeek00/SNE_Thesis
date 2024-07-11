# Written with assistance of generative AI and online community forums.

import random
import string
import json
from kafka import KafkaProducer

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


# Kafka configuration (replace with your details)
bootstrap_servers = "IP HERE:9092"  # Middleware server IP here
topic_name = "Topic1"  # Data stream selection

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
# message_rate = 100 # Messages per second (not used in this example)

while True:  # Continuously generate and publish messages
  message = generate_message()
  json_message = json.dumps(message).encode('utf-8')  # Encode for sending
  producer.send(topic_name, json_message)

producer.close()

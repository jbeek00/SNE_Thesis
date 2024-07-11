#!/bin/bash
# assumes linux debian based OS. 
# Replace link with respective OS if different!
wget https://dlcdn.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz
tar -zxvf kafka_2.13-3.7.0.tgz
cd kafka_2.13-3.7.0/
python3 -m venv kafka_env
source kafka_env/bin/activate # activate environment
pip install kafka-python

echo 'now run "$ bin/zookeeper-server-start.sh config/zookeeper.properties" in one terminal'
echo 'and run "$ bin/kafka-server-start.sh config/server.properties" in another terminal'

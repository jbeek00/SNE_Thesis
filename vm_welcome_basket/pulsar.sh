#!/bin/bash
# assumes linux debian based OS. 
# Replace link with respective OS if different!
wget https://download.oracle.com/java/22/latest/jdk-22_linux-x64_bin.deb
sudo dpkg -i jdk-22_linux-x64_bin.deb

wget https://www.apache.org/dyn/closer.lua/pulsar/pulsar-3.3.0/apache-pulsar-3.3.0-bin.tar.gz?action=download
tar zxvf apache-pulsar-3.3.0-bin.tar.gz\?action\=download
cd apache-pulsar-3.3.0
echo 'export PULSAR_HOME=~/apache-pulsar-3.3.0/' >> ~/.bashrc
echo 'export PATH=$PATH:$PULSAR_HOME/bin' >> ~/.bashrc
source ~/.bashrc
#./$PULSAR_HOME/bin/pulsar-daemon start standalone
python3 -m venv pulsar_env
source pulsar_env/bin/activate # activate environment
echo 'pulsar environment sourced (source pulsar_env/bin/activate'
pip install -y pulsar-client
echo 'pulsar client library installed'



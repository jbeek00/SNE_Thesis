#!/bin/bash
# First script to execute on a configured VM. 
# Script assumes python environments are necessary for script running
apt update
apt install -y net-tools
apt install -y python3-pip
apt install -y python3-venv
apt install -y tree # useful but not essential
# Check root privileges
if [[ $EUID -ne 0 ]]; then
  echo "This script requires sudo privileges."
  exit 1
fi

# Backup the original file
cp /etc/hosts /etc/hosts.bak

# Use sed to modify the line
sed -i '/^127.0.0.1 localhost$/s/localhost$/localhost.localdomain localhost/' /etc/hosts

# Check for successful modification
if grep -q "127.0.0.1 localhost.localdomain localhost" /etc/hosts; then
  echo "Line modified successfully in /etc/hosts"
else
  echo "Modification failed or line not found in /etc/hosts"
fi


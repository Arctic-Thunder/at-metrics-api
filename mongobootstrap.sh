#!/usr/bin/env bash
set -e

# Installation Variables
VENV=metrics-env


sudo apt-get update
sudo apt-get install -y mongodb || echo "Installation Failed" && exit
echo MongoDB installed successfully!

sudo systemctl status mongodb
if [ $? == "0" ]; then
    echo MongoDB service successfully started!
else if [ $? == "3" ]; then
    echo MongoDB service failed to start!
fi

echo Setup Complete!
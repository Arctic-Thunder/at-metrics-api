#!/usr/bin/env bash
set -e

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y python3 python3-venv python3-pip
sudo apt-get install -y virtualenv

# Prepare Django Environment
cd /vagrant

echo Initializing Django Environment
if [ ! -d cscimetrics ]; then
    mkdir cscimetrics
fi
cd cscimetrics

if [ ! -d metrics-env ]; then
    echo -  Creating new virtual environment - metrics-env
    virtualenv -p /usr/bin/python3 metrics-env --always-copy
fi

echo ". /vagrant/cscimetrics/metrics-env/bin/activate" > ~/.profile
echo "cd /vagrant/cscimetrics" >> ~/.profile

source metrics-env/bin/activate
pip install --upgrade
pip install --requirement requirements.txt

echo Setup Complete!
#!/usr/bin/env bash
set -ex

sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-pip

# Prepare Django Environment
cd /vagrant

echo Initializing Django Environment
if [ ! -d cscimetrics ]; then
    mkdir cscimetrics
fi
cd cscimetrics

if [ ! -d metrics-env ]; then
    echo -  Creating new virtual environment - metrics-env
    python3 -m venv metrics-env
fi

echo ". /vagrant/cscimetrics/metrics-env/bin/activate" > ~/.profile
echo "cd /vagrant/cscimetrics" >> ~/.profile

source metrics-env/bin/activate
pip install -r requirements.txt

echo Setup Complete!
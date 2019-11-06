#!/usr/bin/env bash
set -e

# Installation Variables
VENV=~/metrics-env


sudo apt-get update
sudo apt-get install -y python3 virtualenv python3-pip libpq-dev

# Prepare Django Environment
cd /vagrant

echo Initializing Django Environment
# Configure Python Virtual Environment
if [ ! -d $VENV ]; then
    echo - Creating new virtual environment - $VENV
    virtualenv -p $(which python3) $VENV --always-copy

else
    echo - Cleaning old virtual environment - $VENV
    rm -rf $VENV
    virtualenv -p $(which python3) $VENV --always-copy
fi

# Install Python Package Dependencites
echo - Installing Python Packages
source $VENV/bin/activate

if [ -e requirements.txt ]; then
    pip install -r requirements.txt

    cd metrics-root
    ./manage.py makemigrations
    ./manage.py migrate
else
    echo - Missing \"requirements.txt\". Please install requirements manually and execute \"pip freeze > requirements.txt\"
fi

# Configure SSH Login Parameters
echo ". $VENV/bin/activate" > ~/.profile
echo "cd /vagrant/metrics-root" >> ~/.profile

echo Setup Complete!
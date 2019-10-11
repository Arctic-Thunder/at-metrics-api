#!/usr/bin/env bash
set -e

sudo apt-get update
sudo apt-get install -y postgresql postgresql-contrib || echo "Installation Failed" && exit
echo PostgreSQL installed successfully!

# sudo -i -u postgres


echo Setup Complete!
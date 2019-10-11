#!/usr/bin/env bash
set -e

# Perfrom OS Updtes
echo Updating OS Packages...
sudo apt-get update
sudo apt-get upgrade -y
echo Update Complete!
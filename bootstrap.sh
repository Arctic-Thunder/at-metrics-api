#!/usr/bin/env bash
set -e

# Perfrom OS Updtes
echo Updated OS Packages
sudo apt-get update
sudo apt-get upgrade -y
echo $?
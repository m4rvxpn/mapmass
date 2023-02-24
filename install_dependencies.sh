#!/bin/bash

# Install Python 3.x
sudo apt-get update
sudo apt-get install -y python3

# Install Masscan
sudo apt-get install -y git make gcc
git clone https://github.com/robertdavidgraham/masscan
cd masscan
make
sudo make install

# Install Nmap
sudo apt-get install -y nmap

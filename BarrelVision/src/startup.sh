#!/bin/bash

# This script sets up and starts the InkyFrame application

# Navigate to the project directory
cd /home/pi/InkyFrame

# Activate the virtual environment
source env/bin/activate

# Install any necessary dependencies
pip install -r requirements.txt

# Set up the InkyFrame display
python src/display.py setup

# Start the InkyFrame application
python src/main.py
# Rain Alert Project 🌧️

A Python-based weather alert application that checks the forecast using the OpenWeatherMap API and sends SMS notifications via Twilio when rain is expected.

## Features
- Fetches 12-hour weather forecast
- Detects rain conditions based on weather codes
- Sends alert messages to the user via SMS using Twilio

## Technologies Used
- Python
- OpenWeatherMap API
- Twilio API

## Setup
1. Install dependencies: `pip install requests twilio`
2. Replace API keys and phone numbers in `main.py` with your own credentials
3. Run the script: `python main.py`

## Note
This version hides all sensitive information (API keys, phone numbers). Keep your credentials secure.

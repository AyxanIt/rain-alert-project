import requests
import os
from twilio.rest import Client

api_key = "YOUR_OPENWEATHERMAP_API_KEY"
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"
phone_number = "+1234567890"


parameters = {
    "lat": 49.564133,
    "lon": 3.619890,
    "appid": api_key,
    "cnt": 4,
}


link = "api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}"

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 600:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It is going to rain today. Take an umbrella ☔️",
        from_=phone_number,
        to='+994516776500',
    )
    print(message.status)

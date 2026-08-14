import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("WEATHER_API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("Twilio_AUTH_TOKEN")
# "lat" : -22.91,
# "lon" : -43.21,

weather_parameters = {
    "lat" : -22.91,
    "lon" : -43.21,
    "cnt" : 4,
    "appid" : API_KEY
}
response = requests.get(url=OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="Hoje irá chover, é melhor levar um guarda-chuva ☂️",
        from_="whatsapp:+14155238886",  # Your Twilio number
        to="whatsapp:+5521994926351"
    )
    print(message.status)




# https://api.openweathermap.org/data/2.5/weather?lat=-22,91&lon=-43,21&appid=be1c85ecd5f0df76b35205efface99a5
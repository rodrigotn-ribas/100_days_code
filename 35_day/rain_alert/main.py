import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "be1c85ecd5f0df76b35205efface99a5"

# "lat" : -22.91,
# "lon" : -43.21,

weather_parameters = {
    "lat" : 40.71,
    "lon" : -74.00,
    "cnt" : 4,
    "appid" : API_KEY
}
response = requests.get(url=OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")


# https://api.openweathermap.org/data/2.5/weather?lat=-22,91&lon=-43,21&appid=be1c85ecd5f0df76b35205efface99a5
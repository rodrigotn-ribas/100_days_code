from datetime import datetime

import requests

MY_LAT = -22.906847
MY_LNG = -43.172897

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()["iss_position"]

iss_longitude = response.json()["iss_position"]["longitude"]
iss_latitude = response.json()["iss_position"]["iss_latitude"]
iss_position = (iss_longitude, iss_latitude)

print(iss_position)

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LNG,
    "formatted" : 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset= int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)
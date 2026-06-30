import requests
from datetime import datetime

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
# print(iss_longitude, iss_latitude)
# print(MY_LAT, MY_LONG)

lat_dif = (abs(iss_latitude) - abs(MY_LAT))
lng_dif = (abs(iss_longitude) - abs(MY_LONG))
dif_pos = (lat_dif, lng_dif)
#Your position is within +5 or -5 degrees of the ISS position.
if dif_pos[0] >= 5 or dif_pos[0] > 5 or dif_pos[1] < 5 or dif_pos[1] > 5:


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




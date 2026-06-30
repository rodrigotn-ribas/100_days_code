import time
import requests
from datetime import datetime, timezone
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
MY_EMAIL = 'smartcitybots@gmail.com'
MY_PASSWORD = 'ubgc haug eafb dwly '

def is_close():
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
    except requests.RequestException as e:
        print(e)
    else:
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])
        print(iss_latitude, iss_longitude)
        # print(MY_LAT,MY_LONG)

        lat_dif = abs(iss_latitude - MY_LAT)
        lng_dif = abs(iss_longitude - MY_LONG)

        #Your position is within +5 or -5 degrees of the ISS position.
        return MY_LAT <= iss_latitude <= MY_LAT+5 and MY_LONG <= iss_longitude <= MY_LONG+5

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    try:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    except requests.RequestException as e:
        print(e)
    else:
        response.raise_for_status()
        data = response.json()

        sunrise = datetime.fromisoformat(data["results"]["sunrise"])
        sunset = datetime.fromisoformat(data["results"]["sunset"])

        now = datetime.now(timezone.utc)

        return now >= sunset or now <= sunrise

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="rodrigotn.ribas@gmail.com",
            msg=f"Subject:International space station is here\n\n"
                f"Look up, iss is on your sky"
        )

while True:
    if is_close() and is_dark():
        send_email()

    time.sleep(60)




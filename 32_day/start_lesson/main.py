import smtplib
import datetime as dt
import random
from env import *

MY_EMAIL = EMAIL_BOT_HOST
MY_PASSWORD = EMAIL_BOT_PAWSWORD

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt", "r") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="joaomaltar14@gmail.com",
            msg=f"Subject:Monday Motivation\n\n"
                f"{quote}"
        )
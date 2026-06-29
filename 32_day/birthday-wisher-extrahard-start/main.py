##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
from random import choice
import smtplib


MY_EMAIL = 'smartcitybots@gmail.com'
MY_PASSWORD = 'ubgc haug eafb dwly '

# 1. Update the birthdays.csv
birthdays_csv = pd.read_csv("birthdays.csv")
birthdays = pd.DataFrame.to_dict(birthdays_csv)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

today = (month, day)

for _, row in birthdays_csv.iterrows():
    if (row["month"], row["day"]) == today:

        name = row["name"]
        email = row["email"]

        letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt",
                       "letter_templates/letter_3.txt"]

        random_letter = choice(letter_list)

        with open(random_letter) as file:
            letter = file.read()

        send_letter = letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy Birthday\n\n{send_letter}"
            )





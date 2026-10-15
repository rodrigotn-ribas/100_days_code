import requests
import os
from dotenv import load_dotenv
import datetime as dt
from requests.auth import HTTPBasicAuth

load_dotenv()

# Nutrition API
NUTRITION_API_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
APP_ID = os.getenv("x-app-id")
APP_KEY = os.getenv("x-app-key")

# Sheety API
# LINK = "https://api.sheety.co/{username}/{projectName}/{sheetName}"
SHEETY_ENDPOIT = os.getenv("SHEETY_ENDPOIT")
USER = os.getenv("USERNAME_SHEETY")
PASS = os.getenv("PASSWORD_SHEETY")
BASIC = HTTPBasicAuth(USER,PASS) # Autorization

GENDER = "male"
WEIGHT = int(os.getenv("WEIGHT"))
HEIGH = int(os.getenv("HEIGH"))
today = dt.date.today()
born = dt.date(year=2004, month=11, day=8)
AGE = today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def nutrition_post():
  headers = {
      "Content-Type": "application/json",
      "x-app-id": APP_ID,
      "x-app-key": APP_KEY,
    }

  params = {
      "query": input("Tell me which exercices you did: "),
      "weight_kg": WEIGHT,          
      "height_cm": HEIGH, 
      "age": AGE,                        
      "gender": GENDER 
  }

  response = requests.post(url=NUTRITION_API_ENDPOINT, json=params, headers=headers)
  return response.json()


def sheety_get():
  # Filter: ?filter[property]=value; double filter: ?filter[familyFriendly]=true&filter[country]=UK
  response = requests.get(url=f"{SHEETY_ENDPOIT}", auth=BASIC)  
  json = response.json()
  print(json)

def sheety_post(nutri_params):

  params = {
    "workout":{
    "date": dt.datetime.now().strftime("%d/%m/%Y"),
    "time": dt.datetime.now().strftime("%H:%M:%S"),
    "exercise": nutri_params["exercises"][0]["name"].capitalize(),
    "duration": nutri_params["exercises"][0]["duration_min"],
    "calories": nutri_params["exercises"][0]["nf_calories"]
    }
  }
  print(params)

  return requests.post(url=SHEETY_ENDPOIT, json=params, auth=BASIC)  

paramters = nutrition_post()

print(sheety_post(nutri_params=paramters))

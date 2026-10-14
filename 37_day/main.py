import requests
import os
from dotenv import load_dotenv
import datetime as dt

# load env
load_dotenv()
PIXELA_ENDPOINT = "https://pixe.la/v1/users" 
USERNAME = "rodrigoribas"
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Guitar Graph",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)


# POST a pixel in the graph
def pixel_creation_post():
    pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

    today = dt.datetime.now()

    pixel_data = {
        "date":  today.strftime("%Y%m%d"),
        "quantity": input("por quantos minutos vc praticou hj? ")
    }

    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    print(response.text)

# PUT and change a pixel in the graph
def pixel_update_put():
    update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_change}"
    
    date_to_change = dt.datetime(year=2026, month=10, day=12).strftime("%Y%m%d")

    pixel_data_change = {
        "date":  date_to_change,
        "quantity": "120"
    }

    response = requests.put(url=update_endpoint, json=pixel_data_change, headers=headers)
    print(response.text)

def pixel_delete():
    today = dt.datetime.now()
    delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)


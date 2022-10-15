# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_data = FlightData()
notification_manager = NotificationManager()

sheety_api_endpoint = "https://api.sheety.co/5049260a3632bb7a599da36651c413bf/flightDeals/prices"

SHEETY_AUTH = {
    "Authorization": "Basic WmFtYmk6WmFtYmlycnJ0ODU3QEA"
}

sheety_response = requests.get(url=sheety_api_endpoint, headers=SHEETY_AUTH)
sheety_response.raise_for_status()
sheet_data = sheety_response.json()["prices"]
data_manager.row_update(sheet_data)

for city in sheet_data:
    try:
        # text: str
        price, text = flight_data.get_data(city["iataCode"])
        if city["lowestPrice"] >= price:
            notification_manager.send_notification(text)
    except TypeError:
        continue







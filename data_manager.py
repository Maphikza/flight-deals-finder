import requests
from flight_search import FlightSearch

SHEETY_AUTH = {
    "Authorization": "Basic WmFtYmk6WmFtYmlycnJ0ODU3QEA"
}
search = FlightSearch()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = None
        self.sheet_endpoint = "https://api.sheety.co/5049260a3632bb7a599da36651c413bf/flightDeals/prices"
        self.AUTH = SHEETY_AUTH

    def row_update(self, data):
        for i in range(len(data)):
            row = {
                "price": {
                    "iataCode": search.city_search(data[i]["city"]),
                }
            }
            if data[i]["iataCode"] == '':
                self.response = requests.put(
                    url=f"https://api.sheety.co/5049260a3632bb7a599da36651c413bf/flightDeals/prices/{data[i]['id']}",
                    headers=self.AUTH, json=row)
                self.response.raise_for_status()
                print(self.response.status_code)
            else:
                pass

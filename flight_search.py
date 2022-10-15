import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.search_end_point = "tequila-api.kiwi.com/"
        self.location_end_point = "https://tequila-api.kiwi.com/locations/query"
        self.api_key = "qCWsCSFJLN0MgCFWqF2kXCUXaO21u5gb"
        self.id = None
        self.params = None
        self.header = None
        self.response = None

    def city_search(self, city: str):
        self.params = {
            "term": city,
            "location_types": "city",
            "limit": 1,
        }

        self.header = {
            "apikey": self.api_key
        }
        self.response = requests.get(url=self.location_end_point, params=self.params, headers=self.header)
        self.response.raise_for_status()
        flight_data = self.response.json()
        return flight_data["locations"][0]["code"]


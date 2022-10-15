import requests
from datetime import datetime
from datetime import timedelta
from pprint import pprint


class FlightData:

    def __init__(self):
        self.start_date = datetime.now() + timedelta(days=+1)
        self.end_date = self.start_date + timedelta(days=6 * 30)
        self.api_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.api_key = "qCWsCSFJLN0MgCFWqF2kXCUXaO21u5gb"
        self.parameters = None
        self.header = {
            "apikey": self.api_key
        }

    def get_data(self, destination):
        try:
            self.parameters = {
                "fly_from": "CPT",
                "fly_to": destination,
                "flight_type": "round",
                "date_from": self.start_date.strftime("%d/%m/%Y"),
                "date_to": self.end_date.strftime("%d/%m/%Y"),
                "curr": "ZAR",
                "adults": 1,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "one_for_city": 1,
                "max_stopovers": 0,
            }

            response = requests.get(url=self.api_endpoint, params=self.parameters, headers=self.header)
            response.raise_for_status()
            data = response.json()
            arrival_city = data["data"][0]["cityTo"]
            arrival_city_iata = data["data"][0]["flyTo"]
            depart_city = data["data"][0]["cityFrom"]
            depart_city_iata = data["data"][0]["flyFrom"]
            price = data["data"][0]["price"]
            departure_date = data["data"][0]["route"][0]["local_arrival"].split("T")[0]
            return_date = data["data"][0]["route"][1]["local_arrival"].split("T")[0]
            message = f"Low price alert! Only ZAR{price} to fly from {depart_city}-{depart_city_iata} to {arrival_city}-{arrival_city_iata}, from {departure_date} to {return_date}, To make a a booking, click here: {data['data'][0]['deep_link']}"
            print(f"{arrival_city}: {price}")
            return price, message

        except IndexError:
            self.parameters = {
                "fly_from": "CPT",
                "fly_to": destination,
                "flight_type": "round",
                "date_from": self.start_date.strftime("%d/%m/%Y"),
                "date_to": self.end_date.strftime("%d/%m/%Y"),
                "curr": "ZAR",
                "adults": 1,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                # "one_for_city": 1,
                # "max_stopovers": 1,
            }
            response = requests.get(url=self.api_endpoint, params=self.parameters, headers=self.header)
            response.raise_for_status()
            data = response.json()
            depart_city = data["data"][0]["cityFrom"]
            depart_city_iata = data["data"][0]["flyFrom"]
            price = data["data"][0]["price"]
            departure_date = data["data"][0]["route"][0]["utc_departure"].split("T")[0]
            return_date = data["data"][0]["route"][1]["utc_arrival"].split("T")[0]
            # pprint(data["data"][0])
            # pprint(data["data"][0]["route"])
            stops = len(data["data"][0]["route"]) - 2
            route = []
            for i in range(len(data["data"][0]["route"])):
                route.append(data["data"][0]["route"][i]["cityFrom"])
                route.append(data["data"][0]["route"][i]["cityTo"])
            route_length = len(data["data"][0]["route"]) * 2
            final_route = [route[n] for n in range(0, route_length, 2)]
            # final_route_str = '- '.join(final_route)
            message = f"Low price alert! Only ZAR{price} to fly from {depart_city}-{depart_city_iata} to {data['data'][0]['cityTo']}-{data['data'][0]['flyTo']}, from{departure_date} to {return_date}. This flight has {stops} stop overs in total. To find out more about the route and booking, click here: {data['data'][0]['deep_link']} "
            print(f"{data['data'][0]['cityTo']}: {price}")
            return price, message


# flight_data = FlightData()
# flight_data.get_data(destination="DPS")

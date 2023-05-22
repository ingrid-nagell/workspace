from datetime import datetime, timedelta
import requests

VAR_PATH = "C:\\Users\\G020772\\repos\\python_env_vars.txt"
with open(VAR_PATH, "r") as f:
    keys = dict(l.strip().split(": ") for l in f)

TEQUILA_ENDPOINT = "http://api.tequila.kiwi.com"
TEQUILA_API_KEY = keys["TEQUILA_API_KEY"]

ORIGIN_CITY_IATA = "OSL"


class FlightSearch():

    def get_iata_codes(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        code = response.json()["locations"][0]["code"]
        return code
    
    def get_flights(self, city, max_price):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        departure_time_first = datetime.strftime(datetime.now() + timedelta(days=7), '%d/%m/%Y')
        departure_time_last = datetime.strftime(datetime.now() + timedelta(days=37), '%d/%m/%Y')
        query = {
            "fly_from": ORIGIN_CITY_IATA,
            "fly_to": city,
            "date_from": departure_time_first,
            "date_to": departure_time_last,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 7,
            "adults": 1,
            "curr": "NOK",
            "price_to": max_price,
            "max_stopovers": 0,
            "limit": 100,
        }
        response = requests.get(url=search_endpoint, headers=headers, params=query)
        data = response.json()["data"]
        cheapest_flight = self.cheapest_flight(data=data, max_price=max_price)
        return cheapest_flight
    
    def cheapest_flight(self, data, max_price):
        lowest_price = max_price
        cheapest_flight = {}
        for flight in data:
            if flight["price"] < lowest_price:
                cheapest_flight = flight
                lowest_price = flight["price"]
        return cheapest_flight
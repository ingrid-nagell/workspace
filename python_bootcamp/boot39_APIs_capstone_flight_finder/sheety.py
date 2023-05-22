from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH
import requests

VAR_PATH = "C:\\Users\\G020772\\repos\\python_env_vars.txt"
with open(VAR_PATH, "r") as f:
    keys = dict(l.strip().split(": ") for l in f)

SHEETY_USERNAME = keys["SHEETY_USERNAME"]
SHEETY_PROJECT_NAME = "flightDeals"
SHEETY_SHEETNAME = "prices"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEETNAME}"
SHEETY_HEADER = {"Authorization": keys["SHEETY_AUTH"]}

class SheetyContentCreator():

    def create_content(self, destinations, iata_func):
        """Function for addeing new rows to the Google Sheet project."""
        for key, value in destinations.items():
            report = {
                "price": {
                    "city": key,
                    "iataCode": iata_func(key),
                    "lowestPrice": value,
                }
            }
            r = requests.post(url=SHEETY_ENDPOINT, json=report, headers=SHEETY_HEADER)
            print(r.status_code)
    
    def get_content(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADER)
        data = response.json()
        return data["prices"]

# sheety = SheetyContentCreator()
# r = sheety.get_content()
# print(r)
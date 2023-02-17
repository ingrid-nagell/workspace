import requests
import os

tokens = {}
with open('C:\\Users\\G020772\\repos\\secrets.txt', 'r') as f:
    for l in f:
        items = l.split(',')
        key, value = items[0], items[1]
        tokens[key] = value

def check_for_rainfall():
    api_key = tokens['OWS']
    endpoint_hourly = "https://api.openweathermap.org/data/2.5/forecast"
    parameters = {
        "lat": 62.737709,
        "lon": 7.160910,
        "appid": api_key,
    }

    response = requests.get(endpoint_hourly, params=parameters)
    response.raise_for_status()

    will_rain = False

    for n in range(0,2):
        if response.json()['list'][n]['weather'][0]['id'] > 499:
            will_rain = True

    if will_rain:
        print("Bring an umbrella.")

print(check_for_rainfall())
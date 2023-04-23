import requests
from datetime import datetime, time
import os

#os.environ["NUTRI_APP_ID"] = "11e01bf2"
# cannot add new vars to os...

VAR_PATH = "C:\\Users\\G020772\\repos\\workspace\\python_env_vars.txt"
with open(VAR_PATH, "r") as f:
    keys = dict(l.strip().split(": ") for l in f)

NUTRI_APP_ID = keys["NUTRI_APP_ID"]
NUTRI_API_KEY = keys["NUTRI_API_KEY"]

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_header = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY
}

query_input = "One hour of weight training and 20 min of jogging"
# query_input = input("What excersise did you do? ")

exercise_config = {
    "query": query_input,
    "gender": "female",
    "weight_kg": 65.2,
    "height_cm": 169.6,
    "age": 31
}

r = requests.post(url=EXERCISE_ENDPOINT, json=exercise_config, headers=nutri_header)
data = r.json()["exercises"]

SHEETY_USERNAME = keys["SHEETY_USERNAME"]
SHEETY_PROJECT_NAME = "workouts"
SHEETY_SHEETNAME = "workouts"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEETNAME}"
SHEETY_HEADER = {
   "Authorization": keys["SHEETY_AUTH"]
}

current_time = datetime.now()

for elem in data:
    report = {
        "workout": {
            "date": current_time.strftime("%d/%m/%Y"),
            "time": current_time.strftime("%X"),
            "exercise": elem["user_input"],
            "duration": elem["duration_min"],
            "calories": elem["nf_calories"], 
            }
    }

    sheety_r = requests.post(url=SHEETY_ENDPOINT, json=report, headers=SHEETY_HEADER)
    # print(sheety_r.text)
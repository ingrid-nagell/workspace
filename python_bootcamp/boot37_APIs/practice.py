# requests.get() -- ask external service for data
# request.post() -- send data, get status
# request.put() -- update external service
# request.delete() -- delete data in external service

import requests
from datetime import datetime

VAR_PATH = "C:\\Users\\G020772\\repos\\workspace\\python_env_vars.txt"
with open(VAR_PATH, "r") as f:
    keys = dict(l.strip().split(": ") for l in f)


USERNAME = keys["PIXELA_USER"]
TOKEN = keys["PIXELA_TOKEN"]
GRAPH_ID = "graph"

endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#r = requests.post(url=endpoint, json=user_params)
#print(r.json)

graph_endpoint = f"{endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Graphy",
    "unit": "km",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# r = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(r.text)

now = datetime.now().strftime("%Y%m%m")
quantity = "23"

pix_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pix_config = {
    "date": now,
    "quantity": quantity,
}

r = requests.post(url=pix_endpoint, json=pix_config, headers=headers)
print(r.text)
# Build a Flight Club for cheap flight deals, with end users
import requests

VAR_PATH = "C:\\Users\\G020772\\repos\\secrets.txt"
with open(VAR_PATH, "r") as f:
    keys = dict(l.strip().split(": ") for l in f)

SHEETY_USERNAME = keys["SHEETY_USERNAME"]
SHEETY_PROJECT_NAME = "flightProject"
SHEETY_SHEETNAME = "members"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEETNAME}"
SHEETY_HEADER = {"Authorization": keys["SHEETY_AUTH"]}


# r = requests.get(url=SHEETY_ENDPOINT)
# print(r.text)

first_name = input("Welcome to the flight club.\nWhat is you first name?\n").capitalize()
last_name = input("What is your last name?\n").capitalize()
email = input("What is your email?\n").lower()
email_confirm = input("Type your email again.\n").lower()

ask_again = True

while ask_again:
    if email == email_confirm:
        ask_again = False
        report = {
            "member": {
                "firstName": first_name,
                "lastName": last_name,
                "eMail": email
            }
        }
    else:
        email_confirm = input("Wrong input. Type your email again.\n").lower()

r = requests.post(url=SHEETY_ENDPOINT, json=report, headers=SHEETY_HEADER)
print(r.status_code)
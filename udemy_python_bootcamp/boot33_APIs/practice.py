# Application Programming Interfaces

# JSON: Created for JavaScript, but now the go to data format for transferring data across the internet.

#Endpoints: Location, ususally an URL
#Requests: 
#Calls:

# Response codes provides information on our request.
# httpstatuses.com
# 1xx: Hold on
# 2xx: Successful
# 3xx: Not permission to request
# 4xx: Error on client side
# 5xx: Error on web side

import requests
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# data = response.json()
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# print(longitude, latitude)

MY_LAT = 62.728360
MY_LONG = 7.296050

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

#To view: https://api.sunrise-sunset.org/json?PARAM1&PARAM2

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status() # Raise exception if not 2xx status code

data = response.json()
print(data['results']['sunrise'].split('T')[1].split(':')[0])
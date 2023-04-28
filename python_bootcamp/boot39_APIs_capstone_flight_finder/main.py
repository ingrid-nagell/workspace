# Flight Deal finder

from flight_search import FlightSearch
from sheety import SheetyContentCreator

# Create sheet:
new_destinations = {
    "Amsterdam": 300,
    "Oslo": 500,
    "Molde": 1000,
}

sheety = SheetyContentCreator()
flight_search = FlightSearch()

# Add new rows to Google sheet:
# sheety.create_content(new_destinations, flight_search.get_iata_codes)

# Get info about destinations from Google sheets
content = sheety.get_content()

# Search flights
for elem in content:
    city = elem["city"]
    code = elem["iataCode"]
    max_price = elem["lowestPrice"]
    flight_data = flight_search.get_flights(code, max_price)
    try:
        print(
            f"* Travel to {city} for {flight_data['price']} NOK!\n",
            f"Duration to destination: {round(flight_data['duration']['departure']/60/60, 2)}\n",
            f"Duration return: {round(flight_data['duration']['return']/60/60, 2)}\n",
            f"Available seats: {flight_data['availability']['seats']}\n",
            f"Nights in destination: {flight_data['nightsInDest']}\n",
            f"Departure, local time: {flight_data['route'][0]['local_departure']}\n",
            f"Departure return, local time: {flight_data['route'][1]['local_departure']}\n",
        )
    except KeyError:
        print(f"* No cheap flights found for {city}\n")
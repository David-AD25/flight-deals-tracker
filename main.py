#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests_cache 
from datetime import datetime, timedelta
 

 # ==================== Conserve requests and preserve your free plan ====================
# Here we are not caching anything ending in *.sheety.co
# everything else is cached for 1 hour (3600 seconds).

requests_cache.install_cache(
    'flight_cache',              # file name (creates flight_cache.sqlite)
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,  # cache duration

    }
)

from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager




# ==================== Talk to Sheety ====================
from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
for destination in sheet_data:
    print(f"{destination['city']}: ID = {destination['id']}")
# print(sheet_data)




# ==================== Set the Dates ====================
 
tomorrow = (datetime.now() +  timedelta(days=1)).strftime("%Y-%m-%d")

six_months_later = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")



# ==================== Do a Flight Search ====================

flight_search = FlightSearch()

flights= flight_search.check_flights(
    origin_city_code="LHR",
    destination_city_code= "CDG",
    from_time= tomorrow, 
    to_time= six_months_later,

)



# ==================== Search all the destinations ====================

# Set your origin airport (London Heathrow)
ORIGIN_CITY_IATA = "LHR"

# For each row in the google sheet, check flights using serpapi, with parameters : airport codes for the origin and destination city, from the current date and a date 6 months later 
# It then  searches for flights for all the desitinations 
for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_later
    )


    # ==================== Show the Cheapest Flight ====================

    cheapest_flight = find_cheapest_flight(flights, return_date=six_months_later)
    pprint(f"{destination['city']}: GBP {cheapest_flight.price}")
    notif_manager = NotificationManager()

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination['city']}!")
        print(f"Updating row ID: {destination['id']}")
        data_manager.update_lowest_price(sheet_data[0]["id"], cheapest_flight.price)
        notif_manager.send_notif(price=cheapest_flight.price, departure_airport_IATA=ORIGIN_CITY_IATA, arrival_airport_IATA=destination["iataCode"], outbound_date= tomorrow, inbound_date=six_months_later)
        

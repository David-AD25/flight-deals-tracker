import requests
import os 
from dotenv import load_dotenv

load_dotenv()

endpoint = "https://serpapi.com/search?engine=google"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self._api_key = os.getenv("SERP_API_KEY")
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
    
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self._api_key,
            
        }

        response = requests.get(url= endpoint, params= query)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print(response.text)
            return None

        data = response.json()
        if "error" in data:
            print(response.text)
            print(f"API error: {data['error']}")
            return None
        return data



pass
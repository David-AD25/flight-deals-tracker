import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/8d3b72af617fba35e5593e52c015ecae/flightPrices/sheet1"
SHEETY_PRICES_UPDATE_ENDPOINT = "https://api.sheety.co/8d3b72af617fba35e5593e52c015ecae/flightPrices/sheet1"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self._user = os.environ["USERNAME"]
        self._password = os.environ["PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}


    def get_destination_data(self):
            # 2. Use the Sheety API to GET all the data in that sheet and print it out.
            response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
            data = response.json()
            self.destination_data = data["sheet1"]
            # print(data)
            return self.destination_data
    
    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "sheet1": {
                "lowest_price": new_price
            }

        }
        response = requests.put(
            url=f"{SHEETY_PRICES_UPDATE_ENDPOINT}/{row_id}",
            json=new_data,
            auth=self._authorization
        )
        
        # Check if it actually worked
        print(f"Update response: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code != 200:
            print(f"Failed to update row {row_id}")
    

# response = requests.get(url=SHEETY_PRICES_ENDPOINT)
# data = response.json()
# print(data["lowestPrice"])
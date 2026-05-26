import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os


load_dotenv()



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.TWILIO_SID=os.getenv("TWILIO_SID")
        self.TWILIO_AUTH_TOKEN=os.getenv("TWILIO_AUTH_TOKEN")
        self.TWILIO_VIRTUAL_NUMBER=os.getenv("TWILIO_VIRTUAL_NUMBER")
        self.TWILIO_WHATSAPP_NUMBER=os.getenv("TWILIO_WHATSAPP_NUMBER")

    def send_notif(self, price,  departure_airport_IATA, arrival_airport_IATA, outbound_date, inbound_date):

        client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)
        self.message = client.messages.create(
        from_=f"whatsapp:{self.TWILIO_VIRTUAL_NUMBER}",
        body=f" 🛩️🌍 Low price alert! Only £{price} to fly from {departure_airport_IATA} to {arrival_airport_IATA}, on {outbound_date} until {inbound_date}",
        to=f"whatsapp:{self.TWILIO_WHATSAPP_NUMBER}"
        )
       
        







pass
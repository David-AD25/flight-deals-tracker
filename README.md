# Flight Deals Tracker

Automated flight price tracker that searches for cheaper flights and sends WhatsApp notifications via Twilio.

## Features
- Searches flights using Google Flights API (SerpAPI)
- Compares prices against your target price in a Google Sheet
- Sends WhatsApp notifications when cheaper flights are found
- Caches API responses to save requests

## Setup
1. Clone the repo
2. Create a `.env` file with your API keys:
   - SERP_API_KEY (SerpAPI)
   - TWILIO_SID, TWILIO_AUTH_TOKEN, etc.
   - USERNAME, PASSWORD (Sheety credentials)
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python main.py`

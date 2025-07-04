from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()   # Loads variables from .env into environment

api_key = os.getenv("API_KEY")  # API key stored in local .env file
print(f"Your API key is: {api_key}")

# Mock data used to test features before implementing actual API calls with a key
# Response is the JSON given as example response on rapidapi
def testAPI():
    with open("mock_flight_response.json", "r") as f:
        data = json.load(f)
    
    return data["data"]["flightOffers"]


if __name__ == "__main__":
    mock_data = testAPI()
    #print(mock_data)
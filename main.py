import os
import requests
import json
import config


# API querystring that imports the parameters set in the config.py file
# -------- IMPORTANT ---------
# If you left any of the optional parameters in config.py blank such as "children", or if it has a value but you want to omit it
# then you must comment it out of the querystring dict below.
querystring = {
    "departure_id": config.DEPARTURE_ID,   # REQUIRED PARAMETER
    "arrival_id": config.ARRIVAL_ID,   # REQUIRED PARAMETER
    "outbound_date": config.OUTBOUND_DATE,   # REQUIRED PARAMETER
    "return_date": config.RETURN_DATE,
    "travel_class": config.TRAVEL_CLASS,
    "adults": config.ADULTS,
    "children": config.CHILDREN,
    "infant_on_lap": config.INFANT_ON_LAP,
    "infant_in_seat": config.INFANT_IN_SEAT,
    "show_hidden": config.SHOW_HIDDEN,
    "currency": config.CURRENCY,
    "language_code": config.LANGUAGE_CODE,
    "country_code": config.COUNTRY_CODE
}

# Mock data used to test features before implementing actual API calls with a key
# Response is the JSON given as example response on rapidapi
def mockAPI():
    with open("mock_search_flights_response.json", "r") as f:
        data = json.load(f)
    
    return data["data"]["topFlights"]

def searchFlightOffers(data):
    option = 0
    for top_flights in data:
        #for segments in flight["segments"]:
            #for legs in segments["legs"]:
                #pass

        print(f"Flight: {option}; Total Price: {top_flights["price"]} {config.CURRENCY}")
        print()
        option += 1


if __name__ == "__main__":
    mock_data = mockAPI()
    #print(mock_data)
    #print(querystring)
    searchFlightOffers(mock_data)
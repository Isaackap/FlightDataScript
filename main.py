import os
import requests
import json
import config


# API querystring that imports the parameters set in the config.py file
# -------- IMPORTANT ---------
# If you left any of the optional parameters in config.py blank such as "children", or if it has a value but you want to omit it
# then you must comment it out of the querystring dict below.
querystring = {
    "fromId": config.FROM_ID,   # REQUIRED PARAMETER
    "toId": config.TO_ID,   # REQUIRED PARAMETER
    "departDate": config.DEPART_DATE,   # REQUIRED PARAMETER
    "returnDate": config.RETURN_DATE,
    "stops": config.STOPS,
    "pageNo": config.PAGE_NO,
    "adults": config.ADULTS,
    "children": config.CHILDREN,
    "sort": config.SORT,
    "cabinClass": config.CABIN_CLASS,
    "currency_code": config.CURRENCY_CODE
}

# Mock data used to test features before implementing actual API calls with a key
# Response is the JSON given as example response on rapidapi
def mockAPI():
    with open("mock_flight_response.json", "r") as f:
        data = json.load(f)
    
    return data["data"]["flightOffers"]

def searchFlightOffers(data):
    segment = 0
    for flight in data:
        #for segments in flight["segments"]:
            #for legs in segments["legs"]:
                #pass

        print(f"Flight: {segment}; Total Price: {flight["priceBreakdown"]["total"]["units"]} {config.CURRENCY_CODE}")
        print()
        segment += 1


if __name__ == "__main__":
    mock_data = mockAPI()
    #print(mock_data)
    #print(querystring)
    searchFlightOffers(mock_data)
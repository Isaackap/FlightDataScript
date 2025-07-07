import os
import requests
import json
import config


# API querystring that imports the parameters set in the config.py file
# -------- IMPORTANT ---------
# If you left any of the optional parameters in config.py blank such as "children", or if it has a value but you want to omit it
# then you must comment it out of the querystring dict below.
querystring = {
    "sourceAirportCode": config.SOURCE_AIRPORT_CODE,                # REQUIRED PARAMETER
    "destinationAirportCode": config.DESTINATION_AIRPORT_CODE,      # REQUIRED PARAMETER
    "date": config.DEPARTURE_DATE,                                  # REQUIRED PARAMETER
    "itineraryType": config.ITINERARY_TYPE,                         # REQUIRED PARAMETER
    "sortOrder": config.SORT_ORDER,                                 # REQUIRED PARAMETER
    "numAdults": config.NUM_ADULTS,                                 # REQUIRED PARAMETER
    "numSeniors": config.NUM_SENIORS,                               # REQUIRED PARAMETER
    "classOfService": config.CLASS_OF_SERVICE,                      # REQUIRED PARAMETER
    "returnDate": config.RETURN_DATE,                               # OPTIONAL
    "pageNumber": config.PAGE_NUMBER,                               # OPTIONAL
    "childAges": config.CHILD_AGES,                                 # OPTIONAL
    "nearby": config.NEARBY,                                        # OPTIONAL
    "nonstop": config.NONSTOP,                                      # OPTIONAL
    "currencyCode": config.CURRENCY_CODE,                           # OPTIONAL
    "airlines": config.AIRLINES,                                    # OPTIONAL
    "bookingSites": config.BOOKING_SITES,                           # OPTIONAL
    "region": config.REGION                                         # OPTIONAL
}

# Mock data used to test features before implementing actual API calls with a key
# Response is the JSON given as example response on rapidapi
def mockAPI():
    with open("mock_search_flights_response.json", "r") as f:
        data = json.load(f)
    
    return data["data"]["flights"]

def searchFlightOffers(data):
    option = 0
    for flight in data:
        #for segments in flight["segments"]:
            #for legs in segments["legs"]:
                #pass

        print(f"Flight: {option}; Total Price: {flight["purchaseLinks"][""]} {config.CURRENCY_CODE}")
        print()
        option += 1


if __name__ == "__main__":
    mock_data = mockAPI()
    #print(mock_data)
    #print(querystring)
    searchFlightOffers(mock_data)
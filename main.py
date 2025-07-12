import os
import requests
import json
import config
import smtplib
from email.message import EmailMessage

# Function to build and send the email of the price alerts
# Pulls all the parameters from the config file except the main message/body of the email
def sendEmail():
    msg = EmailMessage()
    with open("flight_data.txt", "r") as f:
        message = f.read()
    
    msg["From"] = config.FROM_EMAIL
    msg["To"] = config.TO_EMAIL
    msg["Subject"] = config.EMAIL_SUBJECT
    msg.set_content(message)
    
    with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(config.FROM_EMAIL, config.EMAIL_PASSWORD)
        server.send_message(msg)
    
        print("Email has been sent to " + config.TO_EMAIL)

# API querystring that imports the parameters set in the config.py file
# -------- IMPORTANT ---------
# If you left any of the optional parameters in config.py blank such as "child_ages", or if it has a value but you want to omit it
# then you must comment it out of the querystring dict below.
'''querystrings = {
    "sourceAirportCode":config.SOURCE_AIRPORT_CODE,                # REQUIRED PARAMETER
    "destinationAirportCode":config.DESTINATION_AIRPORT_CODE,      # REQUIRED PARAMETER
    "date":config.DEPARTURE_DATE,                                  # REQUIRED PARAMETER
    "itineraryType":config.ITINERARY_TYPE,                         # REQUIRED PARAMETER
    "sortOrder":config.SORT_ORDER,                                 # REQUIRED PARAMETER
    "numAdults":config.NUM_ADULTS,                                 # REQUIRED PARAMETER
    "numSeniors":config.NUM_SENIORS,                               # REQUIRED PARAMETER
    "classOfService":config.CLASS_OF_SERVICE,                      # REQUIRED PARAMETER
    "returnDate":config.RETURN_DATE,                               # OPTIONAL
    "pageNumber":config.PAGE_NUMBER,                               # OPTIONAL
    #"childAges":config.CHILD_AGES,                                 # OPTIONAL
    "nearby":config.NEARBY,                                        # OPTIONAL
    "nonstop":config.NONSTOP,                                      # OPTIONAL
    "currencyCode":config.CURRENCY_CODE,                           # OPTIONAL
    #"airlines":config.AIRLINES,                                    # OPTIONAL
    #"bookingSites":config.BOOKING_SITES,                           # OPTIONAL
    "region":config.REGION                                         # OPTIONAL
}'''

querystring = {"sourceAirportCode":"IAH","destinationAirportCode":"HND","date":"2026-01-06","itineraryType":"ROUND_TRIP","sortOrder":"ML_BEST_VALUE","numAdults":"1","numSeniors":"0","classOfService":"ECONOMY","returnDate":"2026-01-16","pageNumber":"1","nearby":"yes","nonstop":"yes","currencyCode":"USD","region":"USA"}


# Mock data used to test features before implementing actual API calls with a key
# Response is the JSON given as example response on rapidapi
def mockAPI() -> list:
    with open("mock_search_flights_response.json", "r") as f:
        data: list = json.load(f)
    
    return data

def callAPI():
    response = requests.get(config.SEARCH_FLIGHTS_API_URL, headers=config.HEADERS, params=querystring)

    data = response.json()

    with open("mock_search_flights_response.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


    return response

# Search through the response data for flight info and prices
def searchFlightOffers(data: list):
    flight_num: int  = 0
    file = open("flight_data.txt", "w+")
    for flight in data:
        option: int = 0
        file.write(f"Flight: {flight_num}:\n")
        for purchaseLink in flight["purchaseLinks"]:
            file.write(f"Option: {option}; Ticket Provider: {purchaseLink["providerId"]}; Total Price: {purchaseLink["totalPrice"]} {config.CURRENCY_CODE}\n")
            option += 1
        flight_num += 1

if __name__ == "__main__":
    #mock_data = mockAPI()
    #data = callAPI()
    print(querystring)
    #print(data)
    #print(querystring)
    #searchFlightOffers(data)
    #sendEmail()
import os
import requests
import json
import config
import smtplib
from email.message import EmailMessage
from datetime import datetime

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
querystring = {
    "fromId":config.SOURCE_AIRPORT_CODE,                           # REQUIRED PARAMETER
    "toId":config.DESTINATION_AIRPORT_CODE,                        # REQUIRED PARAMETER
    "departDate":config.DEPARTURE_DATE,                            # REQUIRED PARAMETER
    "returnDate":config.RETURN_DATE,                               # OPTIONAL
    "stops":config.STOPS,                                          # OPTIONAL
    "pageNo":config.PAGE_NUMBER,                                   # OPTIONAL
    "adults":config.ADULTS,                                        # OPTIONAL
    #"children":config.CHILDREN,                                    # OPTIONAL
    "sort":config.SORT_ORDER,                                      # OPTIONAL
    "cabinClass":config.CABIN_CLASS,                               # OPTIONAL
    "currency_code":config.CURRENCY_CODE,                          # OPTIONAL
}


# Mock data used to test features before implementing actual API calls with a key
# Response is the JSON given as example response on rapidapi
def mockAPI():
    with open("mock_search_flights_response.json", "r") as f:
        data = json.load(f)
    
    return data["data"]["flightOffers"]

def callAPI():
    response = requests.get(config.SEARCH_FLIGHTS_API_URL, headers=config.HEADERS, params=querystring)

    data = response.json()

    with open("mock_search_flights_response.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


    return response, data

# Convert the flight departure/arrival time from timestamp to generic time of day for better interpretation in data sheet
def getTimeOfDay(flightTime: str) -> str:
    dt = datetime.fromisoformat(flightTime)
    hour = dt.hour

    if 4 <= hour < 8:
        return "early morning"
    elif 8 <= hour < 12:
        return "morning"
    elif 12 <= hour < 16:
        return "afternoon"
    elif 16 <= hour < 20:
        return "evening"
    elif 20 <= hour < 24:
        return "night"
    else:
        return "late night"

# Convert the flight duration response from seconds to hours
def getFlightDuration(duration: str) -> str:
    duration_float = float(duration)
    flight_hours = round((duration_float / 3600), 2)

    return str(flight_hours)

# Search through the response data for flight info and prices
def searchFlightOffers(data: dict):
    day_of_week = datetime.now().strftime('%A')
    with open("flight_data.txt", "w+") as file:
        for flightOffers in data:
            segments = flightOffers["segments"][0]
            legs = segments["legs"][0]
            file.write(f"{legs["carriersData"][0]["name"]},{legs["flightInfo"]["flightNumber"]},{segments["departureAirport"]["cityName"]},{segments["departureAirport"]["code"]},{getTimeOfDay(segments["departureTime"])},{len(legs["flightStops"])},{getFlightDuration(segments["totalTime"])},{segments["arrivalAirport"]["cityName"]},{segments["arrivalAirport"]["code"]},{getTimeOfDay(segments["arrivalTime"])},{legs["cabinClass"]},{flightOffers["tripType"]},{flightOffers["priceBreakdown"]["total"]["currencyCode"]},{flightOffers["priceBreakdown"]["total"]["units"]},{day_of_week}\n")

if __name__ == "__main__":
    mock_data = mockAPI()

    '''response, data = callAPI()
    if response.ok:
        searchFlightOffers(data)
    else:
        print(f"SearchFlight response returned False with status code: {response.status_code}")
        try:
            error_json = response.json()
            print("Message: ", error_json.get("message", "No message provided."))
        except ValueError:
            print("Raw error: ", response.text)'''
    
    searchFlightOffers(mock_data)
    #sendEmail()
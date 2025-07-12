import os
from dotenv import load_dotenv

load_dotenv() # Loads variables from .env into environment

# ------------------------------------------------------------- Email Configurations Below ------------------------------------------------------------

# Parameters for sending the email/alert of flight offers.
# The Sender and Receiver email info will be imported from the local .env file as well as the Sender email password (Use app password if 2FA is enabled)
FROM_EMAIL = os.getenv("SENDER_EMAIL")
TO_EMAIL = os.getenv("RECEIVER_EMAIL")
EMAIL_PASSWORD = os.getenv("PASSWORD")
# Parameters for the email server, only variable that needs changing is the 'SMTP_SERVER', adjust it to your sender email
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
USE_TLS = "True"
# The subject text of the email, set it to whatever you desire
EMAIL_SUBJECT = "FlightScript Price Alert Test"


# ------------------------------------------------------------- API Configurations below --------------------------------------------------------------

# The 'url' and 'headers' parameters of the "Search Flights" API request
# These should remain constant, the only value that changes is your personal api key that will be loaded from your local .env file
SEARCH_FLIGHTS_API_URL = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"
HEADERS = {
    "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
    "x-rapidapi-host": "tripadvisor16.p.rapidapi.com"
}

# This query takes 20 total parameters, some are optional
# Replace the following variables with the data you desire for your flight search, following the correct format

# Set the desired price point to recieve alerts on flight prices
# Make sure the currency matches the set "CURRENCY_CODE" parameter down below
PRICE_THRESHOLD = 1500

# The airport code (usually 3 letters) and the word 'AIRPORT', separated with a '.'
# Example is the George Bush Intercontinental Airport in Houston, TX. Airport code is 'IAH'"
# From/Departure location Id
SOURCE_AIRPORT_CODE = "IAH"

# To/Arrival location Id, follows same rules as the FROM_ID
DESTINATION_AIRPORT_CODE = "HND"

# Departure or travel date. Format: YYYY-MM-DD
DEPARTURE_DATE = "2026-01-06"

# Pass itineraryType as ONE_WAY for one way and ROUND_TRIP for return flight.
ITINERARY_TYPE = "ROUND_TRIP"

# Sort by parameter. ML_BEST_VALUE, DURATION, PRICE, EARLIEST_OUTBOUND_DEPARTURE, EARLIEST_OUTBOUND_ARRIVAL, LATEST_OUTBOUND_DEPARTURE, LATEST_OUTBOUND_ARRIVAL
SORT_ORDER = "ML_BEST_VALUE"

# The number of guests who are 18-64 years in age. The default value is set to 1
NUM_ADULTS = "1"

# The number of seniors with ago over 65 years old. The default value is set to 1
NUM_SENIORS = "0"

# Specifies the preferred cabin class, such as Economy, Premium Economy, Business, or First Class.
# Available Travel Class: ECONOMY, PREMIUM_ECONOMY, BUSINESS, or FIRST
CLASS_OF_SERVICE = "ECONOMY"

# Return date. Format: YYYY-MM-DD (optional)
RETURN_DATE = "2026-01-16"

# Page number amount, determines how many flight results you get. ~10 flights per page. (optional)
PAGE_NUMBER = "1"

# Pass Children age in the form of Array (Ages between 2-12 years) Eg: [2, 10] (optional)
CHILD_AGES = []

# Include nearby airports (optional)
NEARBY = "yes"

# Prefer nonstop flights (optional)
NONSTOP = "yes"

# Sets the currency for price formatting in the response. (optional)
# Default Value: USD
CURRENCY_CODE = "USD"

# Specifies the region. (optional)
# Either USA, or UK
REGION = "USA"

# Filter by airline. Use comma-separated airline id. Example: KL,JU (optional)
AIRLINES = ""

#Filter by booking sites. Use comma-separated booking sites id. Example: Air Serbia,Austrian Airlines (optional)
BOOKING_SITES = ""

# --------------------------- Completely ommitting these 3 below from the querystring, including here though just in case --------------------------------------

# Pass searchHash from the previous API call to get a complete response (optional)
SEARCH_HASH = ""

# Pass pageLoadUid from the previous API call to get a complete response (optional)
PAGE_LOAD_UID = ""

# Pass searchId from the previous API call to get a complete response (optional)
SEARCH_ID = ""
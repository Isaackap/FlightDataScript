import os
from dotenv import load_dotenv

load_dotenv() # Loads variables from .env into environment

# The 'url' and 'headers' parameters of the "Search Flights" API request
# These should remain constant, the only value that changes is your personal api key that will be loaded from your local .env file
SEARCH_FLIGHTS_API_URL = "https://google-flights2.p.rapidapi.com/api/v1/searchFlights"
HEADERS = {
    "x-rapidapi-host": "google-flights2.p.rapidapi.com",
    "x-rapidapi-key": os.getenv("RAPIDAPI_KEY")
}

# This query takes 13 total parameters, some are optional
# Replace the following variables with the data you desire for your flight search, following the correct format

# Set the desired price point to recieve alerts on flight prices
# Make sure the currency matches the set "CURRENCY_CODE" parameter down below
PRICE_THRESHOLD = 1500

# The airport code (usually 3 letters) and the word 'AIRPORT', separated with a '.'
# Example is the George Bush Intercontinental Airport in Houston, TX. Airport code is 'IAH', so the parameter is "IAH.AIRPORT"
# From/Departure location Id
DEPARTURE_ID = "example.AIRPORT"

# To/Arrival location Id, follows same rules as the FROM_ID
ARRIVAL_ID = "example.AIRPORT"

# Departure or travel date. Format: YYYY-MM-DD
OUTBOUND_DATE = "yyyy-mm-dd"

# Return date. Format: YYYY-MM-DD (optional)
RETURN_DATE = "yyyy-mm-dd"

# Specifies the preferred cabin class, such as Economy, Premium Economy, Business, or First Class. (optional)
# Available Travel Class: ECONOMY, PREMIUM_ECONOMY, BUSINESS, or FIRST
TRAVEL_CLASS = "ECONOMY"

# The number of guests who are 12 years of age or older. The default value is set to 1 (optional)
ADULTS = 1

# The number of children ages 2-11. (optional)
CHILDREN = 0

# The count of infants traveling without a seat, sitting on an adult's lap (ages < 2). (optional)
INFANT_ON_LAP = 0

# The count of infants (below 2 years old) who require a separate seat (optional)
INFANT_IN_SEAT = 0

# Indicates whether hidden should be included in results. (optional)
# Available Options: YES(1) and NO(0)
# Default Value: 0
SHOW_HIDDEN = 1

# Sets the currency for price formatting in the response. (optional)
# Default Value: USD
CURRENCY = "USD"

# Specifies the language in which the response should be returned. (optional)
# Default Value: en-US
LANGUAGE_CODE = "en-US"

# Specifies the country context for filtering and displaying results. (optional)
# Default Value: US
COUNTRY_CODE = "US"
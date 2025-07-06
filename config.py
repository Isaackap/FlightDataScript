import os
from dotenv import load_dotenv

load_dotenv() # Loads variables from .env into environment

# The 'url' and 'headers' parameters of the API request
# These should remain constant, the only value that changes is your personal api key that will be loaded from your local .env file
API_URL = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchFlights"
HEADERS = {
    "x-rapidapi-host": "booking-com15.p.rapidapi.com",
    "x-rapidapi-key": os.getenv("RAPIDAPI_KEY")
}


# The query takes 11 total parameters, some are optional
# Replace the following variables with the data you desire for your flight search, following the correct format

# Set the desired price point to recieve alerts on flight prices
# Make sure the currency matches the set "CURRENCY_CODE" parameter down below
PRICE_THRESHOLD = 1500

# The airport code (usually 3 letters) and the word 'AIRPORT', separated with a '.'
# Example is the George Bush Intercontinental Airport in Houston, TX. Airport code is 'IAH', so the parameter is "IAH.AIRPORT"
# From/Departure location Id
FROM_ID = "example.AIRPORT"

# To/Arrival location Id, follows same rules as the FROM_ID
TO_ID = "example.AIRPORT"

# Departure or travel date. Format: YYYY-MM-DD
DEPART_DATE = "yyyy-mm-dd"

# Return date. Format: YYYY-MM-DD (optional)
RETURN_DATE = "yyyy-mm-dd"

# Filters flights based on the number of stops. Accepted values are: (optional)
# none for no preference (returns flights with any number of stops)
# 0 for non-stop flights
# 1 for one-stop flights
# 2 for two-stop flights
STOPS = 0 

# The page number (optional)
PAGE_NO = 1

# The number of guests who are 18 years of age or older. The default value is set to 1 (optional)
ADULTS = 1

# The number of children, including infants, who are under 18. (optional)
# Example: Child 1 Age = 8 months Child 2 Age = 1 year Child 3 Age = 17 years Here is what the request parameter would look like: children_age: 0,1,17
CHILDREN = 0,1,17

# This parameter orders result by BEST, CHEAPEST or FASTEST flights (optional)
SORT = "BEST"

# Search for flights that match the cabin class specified. Cabin call can be either ECONOMY, PREMIUM_ECONOMY, BUSINESS or FIRST (optional)
CABIN_CLASS = "ECONOMY"

# The currency code (optional)
CURRENCY_CODE = "USD"
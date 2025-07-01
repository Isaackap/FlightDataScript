from dotenv import load_dotenv
import os

load_dotenv()   # Loads variables from .env into environment

api_key = os.getenv("API_KEY")  # API key stored in local .env file
print(f"Your API key is: {api_key}")

'''
if __name__ == "__main__":
    main()
'''
from dotenv import load_dotenv
import os
import requests
import time

# Load environment variables from .env file
load_dotenv()


def fetch_openweathermap_data(location="London", max_retries=3, retry_delay=5):
    # Get the API key from the .env file
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        raise ValueError("OPENWEATHERMAP_API_KEY not found in .env file.")

    # Define the API endpoint
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid=7384172a2fdcc004f0aa2a9aabf0a781&units=metric"

    # Retry logic
    for attempt in range(max_retries):
        try:
            # Send the request
            response = requests.get(api_url, timeout=10)  # Add a timeout to prevent hanging
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries exceeded. Failed to fetch data.")
                return None


if __name__ == "__main__":
    data = fetch_openweathermap_data()
    if data:
        print("Data fetched successfully:")
        print(data)

import requests
import json
from datetime import datetime, timedelta

# Define the API endpoint and your API key
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your api key"

# Define the location for which you want to retrieve the weather forecast
city_name = "Paris"
country_code = "FR"

# Prompt the user to enter a date
target_date_str = input("Enter a date in the format YYYY-MM-DD: ")

# Convert the user-entered date string to a datetime object
target_date = datetime.strptime(target_date_str, "%Y-%m-%d")

# Construct the API request
request_url = f"{api_endpoint}?q={city_name},{country_code}&units=metric&appid={api_key}"

# Send the request and retrieve the response
response = requests.get(request_url)

# Parse the response as JSON
response_data = response.json()

# Extract the forecast data from the response
forecast_data = response_data["list"]

# Initialize the forecast variable to None
forecast = None

# Find the forecast for the target date
for forecast in forecast_data:
    forecast_timestamp = forecast["dt"]
    forecast_date = datetime.fromtimestamp(forecast_timestamp).date()
    if forecast_date == target_date:
        break

# If the forecast variable is still None, set it to a default value
if forecast is None:
    forecast = {"main": {"temp": 0}}

# Extract the temperature from the forecast data
temperature = forecast["main"]["temp"]

# Print the temperature
print(f"The forecasted temperature for {target_date.strftime('%A, %B %d, %Y')} in {city_name} is {temperature}°C.")

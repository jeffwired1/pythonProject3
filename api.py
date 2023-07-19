import requests
import json
from datetime import datetime

API_KEY = '6d2447ce-f577-4896-bf2a-be8711735398'
DEVICE_ID = '222373'
STATION_ID = '84479'



weatherflow_timestamp = 1626706051  # Replace with your actual WeatherFlow timestamp

# Convert the timestamp to a datetime object
dt = datetime.fromtimestamp(weatherflow_timestamp)

# Extract the time component
time_of_day = dt.time()

print(time_of_day)



def get_weather_data():
    url = f'https://swd.weatherflow.com/swd/rest/observations/device/{DEVICE_ID}?api_key={API_KEY}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    return None


def get_forecast_data():
    url = f'https://swd.weatherflow.com/swd/rest/better_forecast?station_id={STATION_ID}&units_temp=f&units_wind=mph&units_pressure=inhg&units_precip=in&units_distance=mi&token={API_KEY}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    return None


# Example usage
#weather_data = get_weather_data()
#if weather_data:
#    print(json.dumps(weather_data, indent=4))
#    print("*******************************************************************")
#else:
#    print("Failed to retrieve weather data.")

forecast_data = get_forecast_data()
if forecast_data:
    # print(json.dumps(forecast_data, indent=4))
    print("*******************************************************************")
else:
    print("Failed to retrieve forecast data.")

weatherflow_timestamp = forecast_data["current_conditions"]["time"]
# Convert the timestamp to a datetime object
dt = datetime.fromtimestamp(weatherflow_timestamp)
# Extract the time component
time_of_day = dt.strftime("%I:%M:%S %p")
print(time_of_day)


# Access the daily forecast
value = forecast_data["forecast"]["daily"]

# individual_dicts = {}
size = 25  # Size of the array
value2 = 0  # Initial value of the array elements
forecast_array = [value2] * size

x = 0
for item in value:
    forecast_array[x] = item
    x = x + 1

print(forecast_array[9])

d = forecast_array[9]["air_temp_low"]
print(d)
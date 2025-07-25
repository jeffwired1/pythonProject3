import requests
from datetime import datetime, timedelta

# ----- User inputs -----
device_id = '222373'  # Replace with your actual device ID
token = '6d2447ce-f577-4896-bf2a-be8711735398'  # Replace with your personal token
date_str = '2025-06-16'  # Desired date in YYYY-MM-DD format

# ----- Convert date to ISO 8601 format -----
start_time = f"{date_str}T00:00:00Z"
end_time = f"{date_str}T23:59:59Z"

# ----- Build the API request URL -----
url = (
    f"https://swd.weatherflow.com/swd/rest/observations/device/{device_id}"
    f"?token={token}&from={start_time}&to={end_time}"
)

# ----- Make the request -----
response = requests.get(url)
data = response.json()

# ----- Display a summary -----
if response.status_code == 200:
    print(url)
    print(f"Data for {date_str}:")
    for obs in data.get('obs', []):
        timestamp = datetime.utcfromtimestamp(obs[0]).strftime('%Y-%m-%d %H:%M:%S')
        temperature_c = obs[7]
        humidity = obs[8]
        print(f"Time: {timestamp} UTC, Temp: {temperature_c:.1f}°C, Humidity: {humidity}%")
else:
    print(f"Error {response.status_code}: {data.get('message', 'Unable to fetch data.')}")
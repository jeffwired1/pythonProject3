import requests
import pandas as pd
from datetime import datetime

# Replace with your actual API key
API_KEY = 'f3b58708498dc05d9679589cfc2ac760'
CITY = 'Laguna Woods,US'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=imperial'

try:
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()

    forecast_list = data.get('list', [])
    if not forecast_list:
        raise ValueError("No forecast data found.")

    forecast_data = []
    for entry in forecast_list:
        dt = datetime.fromtimestamp(entry['dt'])
        temp = entry['main']['temp']
        condition = entry['weather'][0]['description']
        forecast_data.append({
            'Date': dt.strftime('%Y-%m-%d'),
            'Time': dt.strftime('%H:%M'),
            'Temperature (°F)': temp,
            'Condition': condition.title()
        })

    df_forecast = pd.DataFrame(forecast_data)
    print(df_forecast.head(20))  # Show first 20 entries

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except ValueError as ve:
    print(f"Data error: {ve}")
except Exception as ex:
    print(f"Unexpected error: {ex}")
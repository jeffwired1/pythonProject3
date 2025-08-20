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

    print(data)

    forecast_list = data.get('list', [])
    if not forecast_list:
        raise ValueError("No forecast data found.")

    forecast_data = []
    for entry in forecast_list:
        dt = datetime.fromtimestamp(entry['dt'])
        temp = entry['main']['temp']
        feels_like = entry['main']['feels_like']
        humidity = entry['main']['humidity']
        pressure_hpa = entry['main']['pressure']
        pressure_inhg = round(pressure_hpa * 0.02953, 2)
        wind_speed = entry['wind']['speed']
        condition = entry['weather'][0]['description']
        forecast_data.append({
            'Date': dt.strftime('%Y-%m-%d'),
            'Time': dt.strftime('%H:%M'),
            'Temperature (°F)': temp,
            'Feels Like (°F)': feels_like,
            'Humidity %': humidity,
            'Pressure (inHg)': pressure_inhg,
            'Wind Speed (mph)': wind_speed,
            'Condition': condition.title()
        })

    df_forecast = pd.DataFrame(forecast_data)
    df_forecast.to_csv('laguna_woods_forecast.csv', index=False)
    print(df_forecast.head(40))  # Show first 20 entries

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except ValueError as ve:
    print(f"Data error: {ve}")
except Exception as ex:
    print(f"Unexpected error: {ex}")
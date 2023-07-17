import requests
import json

API_KEY = '6d2447ce-f577-4896-bf2a-be8711735398'
DEVICE_ID = '222373'


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


# Example usage
weather_data = get_weather_data()
if weather_data:
    print(json.dumps(weather_data, indent=4))
else:
    print("Failed to retrieve weather data.")

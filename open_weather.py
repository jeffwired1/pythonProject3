import requests
from datetime import datetime


def fetch_weather(api_key, city="Laguna Woods", state="CA", country="US"):
    location = f"{city},{state},{country}"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather = {
            "Location": f"{data['name']}, {state}",
            "Temperature": f"{data['main']['temp']} °F",
            "Feels Like": f"{data['main']['feels_like']} °F",
            "Humidity": f"{data['main']['humidity']}%",
            "Condition": data['weather'][0]['description'].title(),
            "Wind": f"{data['wind']['speed']} mph",
            "Time": datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
        }
        return weather

    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}


def display_weather(weather_data):
    print("\n🌦️ Current Weather Report\n" + "-" * 30)
    for key, value in weather_data.items():
        print(f"{key}: {value}")


# Replace with your actual API key
API_KEY = "f3b58708498dc05d9679589cfc2ac760"

weather = fetch_weather(API_KEY)
display_weather(weather)
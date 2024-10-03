
import requests

def get_weather(api_key, city, state):
    url = "https://api.weather.com/v2/pws/observations/current?stationId=KCALAGUN1276&format=json&units=e&apiKey=f8063d0e05c6478f863d0e05c6e78fbb"
    response = requests.get(url)
    data = response.json()

    current_observation = data["observations"]

    print(current_observation)

    data_list = eval(str(current_observation))
    data_dict = data_list[0]


    # Extract temperature and humidity
    temperature_fahrenheit = data_dict['imperial']['temp']
    humidity_percent = data_dict['humidity']

    print("Temperature:",temperature_fahrenheit,"°F")
    print(f"Humidity: {humidity_percent}%")




if __name__ == "__main__":
    api_key = "f8063d0e05c6478f863d0e05c6e78fbb"
    city = "San Francisco"
    state = "CA"
    get_weather(api_key, city, state)

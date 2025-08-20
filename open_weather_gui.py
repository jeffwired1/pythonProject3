import requests
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from collections import defaultdict

def fetch_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/"
    current_url = f"{base_url}weather?q={city}&appid={api_key}&units=imperial"
    forecast_url = f"{base_url}forecast?q={city}&appid={api_key}&units=imperial"

    try:
        current = requests.get(current_url).json()
        forecast = requests.get(forecast_url).json()

        weather = {
            "Location": f"{current['name']}",
            "Temperature": f"{current['main']['temp']} °F",
            "Feels Like": f"{current['main']['feels_like']} °F",
            "Humidity": f"{current['main']['humidity']}%",
            "Condition": current['weather'][0]['description'].title(),
            "Wind": f"{current['wind']['speed']} mph",
            "Time": datetime.fromtimestamp(current['dt']).strftime('%Y-%m-%d %H:%M:%S')
        }

        daily_forecast = defaultdict(list)
        for entry in forecast['list']:
            dt = datetime.fromtimestamp(entry['dt'])
            date = dt.strftime('%Y-%m-%d')
            time = dt.strftime('%H:%M')
            temp = entry['main']['temp']
            condition = entry['weather'][0]['description'].title()
            daily_forecast[date].append((time, temp, condition))

        # Pick one forecast per day (e.g., closest to noon)
        summarized = []
        for date, entries in daily_forecast.items():
            noonish = min(entries, key=lambda x: abs(int(x[0].split(":")[0]) - 12))
            summarized.append((date, noonish[0], noonish[1], noonish[2]))

        return weather, summarized

    except Exception as e:
        return {"Error": str(e)}, []

def display_weather():
    city = city_entry.get()
    api_key = api_entry.get()
    weather, forecast = fetch_weather(api_key, city)

    output.delete(1.0, tk.END)
    if "Error" in weather:
        output.insert(tk.END, f"Error: {weather['Error']}\n")
        return

    output.insert(tk.END, f"🌤️ Current Weather for {weather['Location']}\n")
    output.insert(tk.END, "-"*40 + "\n")
    for key, value in weather.items():
        output.insert(tk.END, f"{key}: {value}\n")

    output.insert(tk.END, "\n📅 5-Day Forecast\n")
    output.insert(tk.END, "-"*40 + "\n")
    for date, time, temp, condition in forecast:
        output.insert(tk.END, f"{date} {time} — {temp} °F, {condition}\n")

# GUI setup
root = tk.Tk()
root.title("Laguna Woods Weather Forecast")

ttk.Label(root, text="City:").grid(row=0, column=0, sticky="w")
city_entry = ttk.Entry(root, width=30)
city_entry.insert(0, "Laguna Woods")
city_entry.grid(row=0, column=1)

ttk.Label(root, text="API Key:").grid(row=1, column=0, sticky="w")
api_entry = ttk.Entry(root, width=30, show="*")
api_entry.grid(row=1, column=1)

ttk.Button(root, text="Fetch Weather", command=display_weather).grid(row=2, column=0, columnspan=2, pady=10)

output = tk.Text(root, width=60, height=20)
output.grid(row=3, column=0, columnspan=2)

root.mainloop()
import requests
from datetime import datetime, timedelta
import csv
from datetime import date
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide the main window

def confirm_action():
    answer = messagebox.askyesno(title="Confirmation", message=f"Start Date = {start_date_str}\n"
                                                               f"End Date = {end_date_str}")
    if answer:
        print("User confirmed.")
    else:
        print("User canceled.")

start_date_str = simpledialog.askstring("Input", "Enter Start Date as yyyy-mm-dd")
print(f"Start Date = {start_date_str}")
end_date_str = simpledialog.askstring("Input", "Enter End Date as yyyy-mm-dd")
print(f"End Date = {end_date_str}")

today = date.today()
today_str = today.strftime("%Y-%m-%d")

# ----- User inputs -----
device_id = '222373'  # Replace with your actual device ID
token = '6d2447ce-f577-4896-bf2a-be8711735398'  # Replace with your actual token
# start_date_str = '2023-12-29'  # Start date (inclusive)
# end_date_str = '2023-12-31'    # End date (inclusive)
detail_file = 1     # Write out minute by minute data

# ----- Date setup -----
start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
today_date = datetime.strptime(today_str, '%Y-%m-%d')
delta = timedelta(days=1)
offset_days = (today_date - end_date).days
number_days = (end_date - start_date).days + 1
print(f"Number of Days = {number_days}")

confirm_action()

# ----- Log Output file setup -----
filename = 'tempest_log.csv'
filename1 = 'tempest_log_maxmin.csv'
with open(filename, mode='w', newline='') as file, open(filename1, mode='w', newline='') as file1:
    writer = csv.writer(file)
    writer.writerow([
        'Date', 'Time (UTC)', 'Temperature (°F)', 'Humidity (%)',
        'Pressure (inHg)', 'Wind Avg (m/s)', 'Rain (in)',
        'Battery Voltage (V)', 'Heat_index (°F)', 'Indicator',
    ])
    writer1 = csv.writer(file1)
    writer1.writerow([
        'Date', 'Heat Index Max (°F)', 'Heat Index Min (°F)', 'Indicator'
    ])

    # ----- Loop over each day -----
    current = end_date
    offset = offset_days
    while current >= start_date:
        day_str = current.strftime('%Y-%m-%d')
        # from_time = f"{day_str}T00:00:00Z"
        # to_time = f"{day_str}T23:59:59Z"

        url = (
            f"https://swd.weatherflow.com/swd/rest/observations/device/{device_id}"
            f"?day_offset={offset}"
            f"&token={token}"
        )
        # print(url)
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp_max = 0
            temp_min = 200
            for obs in data.get('obs', []):
                timestamp = datetime.utcfromtimestamp(obs[0])
                temp_f = (obs[7] * (9 / 5)) + 32
                humidity = obs[8]
                pressure = 0
                if obs[6] != None:
                    pressure = (obs[6] * 0.02953)
                wind_avg = obs[2]
                rain_in = obs[12] / 25.4
                battery_voltage = obs[16]

                T = temp_f
                RH = humidity
                if temp_f >80 and humidity > 40:
                    heat_index = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                            - 0.22475541 * T * RH - 0.00683783 * T**2
                            - 0.05481717 * RH**2 + 0.00122874 * T**2 * RH
                            + 0.00085282 * T * RH**2 - 0.00000199 * T**2 * RH**2)
                    indicator = 1
                else:
                    heat_index = temp_f
                    indicator = 0

                if temp_max <= heat_index:
                    temp_max = heat_index
                if heat_index <= temp_min:
                    temp_min = heat_index

                if detail_file == 1:
                    writer.writerow([
                        timestamp.date(), timestamp.strftime('%H:%M:%S'),
                        f"{temp_f:.1f}", f"{humidity:.0f}", f"{pressure:.2f}",
                        f"{wind_avg:.2f}", f"{rain_in:.5f}", f"{battery_voltage:.2f}", f"{heat_index:.1f}",
                        indicator,
                    ])

            print(f"Data saved for {timestamp.date()}: Server status code = {response.status_code} = Data Valid!")
        else:
            print(f"Failed to fetch data for {day_str}: {response.status_code}")

        writer1.writerow([
            timestamp.date(), f"{temp_max:.1f}", f"{temp_min:.1f}", indicator,
        ])
        current -= delta
        offset += 1

print(f"\nAll done! Data saved to {filename}")

# https://swd.weatherflow.com/swd/rest/observations/device/222373?day_offset=1&token=6d2447ce-f577-4896-bf2a-be8711735398
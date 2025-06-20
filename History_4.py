import requests
from datetime import datetime, timedelta
import csv
from datetime import date

today = date.today()
today_str = today.strftime("%Y-%m-%d")

# ----- User inputs -----
device_id = '222373'  # Replace with your actual device ID
token = '6d2447ce-f577-4896-bf2a-be8711735398'  # Replace with your actual token
start_date_str = '2025-06-15'  # Start date (inclusive)
end_date_str = '2025-06-19'    # End date (inclusive)

# ----- Date setup -----
start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
today_date = datetime.strptime(today_str, '%Y-%m-%d')
delta = timedelta(days=1)
offset_days = (today_date - end_date).days

# ----- Output file setup -----
filename = 'tempest_log.csv'
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        'Date', 'Time (UTC)', 'Temperature (°F)', 'Humidity (%)',
        'Pressure (inHg)', 'Wind Avg (m/s)', 'Rain (in)',
        'Battery Voltage (V)',
    ])

    # ----- Loop over each day -----
    current = end_date
    offset = offset_days
    while current >= start_date:
        # day_str = current.strftime('%Y-%m-%d')
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
            for obs in data.get('obs', []):
                timestamp = datetime.utcfromtimestamp(obs[0])
                temp_f = (obs[7] * (9 / 5)) + 32
                humidity = obs[8]
                pressure = (obs[6] * 0.02953)
                wind_avg = obs[2]
                rain_in = obs[12] / 25.4
                battery_voltage = obs[16]

                writer.writerow([
                    timestamp.date(), timestamp.strftime('%H:%M:%S'),
                    # timestamp,
                    f"{temp_f:.1f}", f"{humidity:.0f}", f"{pressure:.2f}",
                    f"{wind_avg:.2f}", f"{rain_in:.5f}", f"{battery_voltage:.2f}",
                ])
            print(f"Logged data for {timestamp.date()}")
        else:
            print(f"Failed to fetch data for {day_str}: {response.status_code}")

        current -= delta
        offset += 1

print(f"\nAll done! Data saved to {filename}")

# https://swd.weatherflow.com/swd/rest/observations/device/222373?day_offset=1&token=6d2447ce-f577-4896-bf2a-be8711735398
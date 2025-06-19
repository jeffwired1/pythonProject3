import requests
import datetime

# Replace with your actual token and device_id
API_TOKEN = '6d2447ce-f577-4896-bf2a-be8711735398'
DEVICE_ID = '222373'
START_DATE = datetime.datetime(2025, 6, 1)
END_DATE = datetime.datetime(2025, 6, 10)


def fetch_tempest_data(start, end):
    url = 'https://swd.weatherflow.com/swd/rest/observations/device/'
    headers = {'Authorization': f'Bearer {API_TOKEN}'}
    params = {
        'device_id': DEVICE_ID,
        'start_timestamp': int(start.timestamp()),
        'end_timestamp': int(end.timestamp())
            }
    print(url, headers, params)
    response = requests.get(url, headers=headers, params=params)

    data = response.json()

    for obs in data.get('obs', []):
        print(obs)


fetch_tempest_data(START_DATE, END_DATE)
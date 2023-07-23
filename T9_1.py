import requests

headers = {
    'Authorization': 'Bearer i4Ui6hmlkehICZwQRyqSOA1ikcLh',
    'Content-Type': 'application/json',
}

params = {
    'apikey': 'RFQoRqeKbMJggF1PdsqnyiChU03822ov',
    'locationId': '3228779',
}

json_data = {
    'mode': 'Auto',
    'heatSetpoint': 62,
    'coolSetpoint': 77,
    'autoChangeoverActive': True,
    'thermostatSetpointStatus': 'NoHold',
}

response = requests.post(
    'https://api.honeywell.com/v2/devices/thermostats/LCC-48A2E62503BD',
    params=params,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{\n    "mode": "Auto",\n    "heatSetpoint": 62,\n    "coolSetpoint": 77,\n    "autoChangeoverActive": true,\n    "thermostatSetpointStatus": "NoHold"\n}'
#response = requests.post(
#    'https://api.honeywell.com/v2/devices/thermostats/LCC-48A2E62503BD',
#    params=params,
#    headers=headers,
#    data=data,
#)
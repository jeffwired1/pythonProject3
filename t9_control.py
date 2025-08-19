import requests
import time

class ResideoAPI:
    def __init__(self, client_id, client_secret, redirect_uri, auth_code):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.auth_code = auth_code
        self.access_token = None
        self.refresh_token = None
        self.token_expiry = None

    def authenticate(self):
        url = "https://api.honeywell.com/oauth2/token"
        data = {
            "code": self.auth_code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "grant_type": "authorization_code"
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        tokens = response.json()
        self.access_token = tokens["access_token"]
        self.refresh_token = tokens["refresh_token"]
        self.token_expiry = time.time() + tokens["expires_in"]

    def refresh_access_token(self):
        if time.time() < self.token_expiry - 60:
            return  # Still valid
        url = "https://api.honeywell.com/oauth2/token"
        data = {
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token"
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        tokens = response.json()
        self.access_token = tokens["access_token"]
        self.token_expiry = time.time() + tokens["expires_in"]

    def get_thermostats(self):
        self.refresh_access_token()
        headers = {"Authorization": f"Bearer {self.access_token}"}
        url = "https://api.honeywell.com/v2/devices/thermostats"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def set_temperature(self, device_id, cool_setpoint=None, heat_setpoint=None):
        self.refresh_access_token()
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "coolSetpoint": cool_setpoint,
            "heatSetpoint": heat_setpoint,
            "setpointStatus": "TemporaryHold"
        }
        url = f"https://api.honeywell.com/v2/devices/thermostats/{device_id}/temperature"
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()


#Consumer Key	RFQoRqeKbMJggF1PdsqnyiChU03822ov
#Consumer Secret	XD8tvnpzg5armGUL
#Key Issued	Sun, 07/23/2023 - 06:47
#Key Expires	Never
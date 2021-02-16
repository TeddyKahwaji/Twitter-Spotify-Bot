import requests
import json
import os

REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")
BASE_64 = os.environ.get("BASE_64")


class Refresh:
    def __init__(self):
        self.refresh_token = REFRESH_TOKEN
        self.base_64 = BASE_64

    def refresh(self):
        query = "https://accounts.spotify.com/api/token"
        response = requests.post(query, data={"grant_type": "refresh_token", "refresh_token": REFRESH_TOKEN},
                                 headers={"Authorization": f"Basic {BASE_64}"}).json()
        return response["access_token"]

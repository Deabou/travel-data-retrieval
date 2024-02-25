import requests
from configparser import ConfigParser


class APICall:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def call_api(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint.strip()}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers, params=params)
        return response.json()


class HotelSearch(APICall):
    def __init__(self, base_url, api_key):
        super().__init__(base_url, api_key)

    def search_by_hotels(self, params):
        return self.call_api("by-hotels", params)

    def search_by_city(self, params):
        return self.call_api("by-city", params)

    def search_by_geocode(self, params):
        return self.call_api("by-geocode", params)


class HotelRating(APICall):
    def __init__(self, base_url, api_key):
        super().__init__(base_url, api_key)

    def seach_hotel_sentiment(self, params):
        return self.call_api("hotel-sentiments", params)

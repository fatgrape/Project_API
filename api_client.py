import requests
from config import BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    """GET request"""
    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params)

    """POST request"""
    def post(self, endpoint, data=None):
        return requests.post(f"{self.base_url}{endpoint}", data=data)

    """PUT request"""
    def put(self, endpoint, data=None):
        return requests.put(f"{self.base_url}{endpoint}", data=data)
    
    """DELETE request"""
    def delete(self, endpoint, data=None):
        return requests.delete(f"{self.base_url}{endpoint}", data=data)

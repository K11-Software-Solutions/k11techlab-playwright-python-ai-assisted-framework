import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, **kwargs):
        return requests.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        return requests.post(f"{self.base_url}{endpoint}", data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, json=None, **kwargs):
        return requests.put(f"{self.base_url}{endpoint}", data=data, json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        return requests.delete(f"{self.base_url}{endpoint}", **kwargs)

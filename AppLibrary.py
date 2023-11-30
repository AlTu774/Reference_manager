import requests

class AppLibrary:
    def __init__(self):
        self._base_url = "http://127.0.0.1:5000"

        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/reset")


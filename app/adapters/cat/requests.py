import requests
from app.entities import Uri
from app.interfaces import ICatApi


class RequestsCat(ICatApi):
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get(self) -> Uri:
        response = requests.get("https://api.thecatapi.com/v1/images/search", headers={
            "x-api-key": self.api_key
        })
        if response.status_code != 200:
            raise RuntimeError("Could not get a cat")

        return Uri(response.json()[0]["url"])

import requests


class YaSchedule:
    def __init__(self, api_key: str) -> None:
        if not api_key:
            raise ValueError("Апи ключ не может быть None")
        self.api_key = api_key
        self.base_url: str = "https://api.rasp.yandex-net.ru/v3.0"

    def get_city_info(self, lat: str, lng: str) -> dict:
        request_url = self.base_url + "/nearest_settlement/"
        params = {
            "apikey": self.api_key,
            "lat": lat,
            "lng": lng,
        }
        result = requests.get(url=request_url, params=params)
        return result.json()
    
    def get_schedule(self, from_code: str, to_code: str) -> dict:
        request_url = self.base_url + "/search/"
        params = {
            "apikey": self.api_key,
            "from": from_code,
            "to": to_code,
        }
        result = requests.get(url=request_url, params=params)
        return result.json()

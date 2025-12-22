import requests

from utils import catch_exception


class YaSchedule:
    base_url: str = "https://api.rasp.yandex-net.ru/v3.0"

    def __init__(self, api_key: str) -> None:
        if not api_key:
            raise ValueError("Апи ключ не может быть None")
        
        self.api_key = api_key

    def _make_api_request(
            self, 
            method: str,
            params: dict[str, str]
        ) -> dict:
        request_url = self.base_url + f"/{method}/"
        method_params = params.copy()
        method_params["apikey"] = self.api_key

        return requests.get(
            url=request_url,
            params=method_params,
        ).json()
    
    def _get_city_info(self, lat: str, lng: str) -> dict:
        params = {
            "lat": lat,
            "lng": lng,
        }

        return self._make_api_request(
            method="nearest_settlement",
            params=params,
        )
    
    @catch_exception("Получение расписания")
    def get_schedule(
            self,
            from_lat: str, 
            from_lng: str,
            to_lat: str,
            to_lng: str,
        ) -> dict:
        from_code: str = self._get_city_info(from_lat, from_lng).get("code")
        to_code: str = self._get_city_info(to_lat, to_lng).get("code")

        params = {
            "from": from_code,
            "to": to_code,
        }
        
        return self._make_api_request(
            method="search",
            params=params,
        )

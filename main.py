import os
from dotenv import load_dotenv
from ya_schedule import YaSchedule

load_dotenv()
API_KEY = os.getenv("API_KEY")

schedule_api = YaSchedule(api_key=API_KEY)

kazan_info = schedule_api.get_city_info(lat="55.7887", lng="49.1221")
moscow_info = schedule_api.get_city_info(lat="55.7522", lng="37.6156")
from_code = kazan_info.get("code")
to_code = moscow_info.get("code")
schedule = schedule_api.get_schedule(from_code=from_code, to_code=to_code)
print(schedule.get("segments")[0])
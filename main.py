import os
from dotenv import load_dotenv

from ya_schedule import YaSchedule

load_dotenv()

API_KEY = os.getenv("API_KEY")


schedule_api = YaSchedule(api_key=API_KEY)

schedule = schedule_api.get_schedule(
    from_lat="55.7887",
    from_lng="49.1221",
    to_lat="55.7522",
    to_lng="37.6156",
)
for seg in schedule.get("segments"):
    print(seg.get("arrival"), seg.get("start_date"))
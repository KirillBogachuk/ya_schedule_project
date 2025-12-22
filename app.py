from ya_schedule import YaSchedule

class Application:
    def __init__(self, api_key: str) -> None:
        self.schedule_api = YaSchedule(api_key=api_key)

    def show_menu(self) -> None:
        print("1. Посмртреть расписание")
        print("2. Выход")
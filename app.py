from typing import Optional
from ya_schedule import YaSchedule

class Application:
    def __init__(self, api_key: str, api_key_geo: str) -> None:
        self.schedule_api = YaSchedule(api_key=api_key, api_key_geo=api_key_geo)

    @staticmethod
    def show_menu() -> None:
        print("1. Посмотреть расписание")
        print("3. Выход")

    def __get_schedule(self) -> dict:
        city_from = input("Введите город отправления: ")
        city_to = input("Введите город назначения: ")

        date = input("Введите дату отправления (YYYY-MM-DD): ")
        transport_type = input("Введите тип транспорта: ")
        transfers_input = input("Включать маршруты с пересадками? (д/н): ")
        if transfers_input not in ("yes", "no", "y", "n", "д", "да", "н", "нет"):
            raise ValueError("Нужно ввести один из вариантов (д/н)")

        transfers = False
        if transfers_input == "д" \
                or transfers_input == "да" \
                or transfers_input == "y" \
                or transfers_input == "yes":
            transfers = True

        return self.schedule_api.get_schedule(
            city_from=city_from,
            city_to=city_to,
            date=date,
            transport_types=transport_type,
            transfers=transfers,
        )

    def __show_schedule(self, schedule_info: Optional[dict]) -> None:
        if not schedule_info:
            print("Не удалось получить расписание. Попробуйте снова.")
            return

        counter = 1
        for sch in schedule_info.get("segments", []):
            print(f"{counter}. {sch.get("thread").get('title')} - {sch.get('thread').get('number')}")
            print(f"\t{sch.get("thread").get("transport_type")} - {sch.get("thread").get("vehicle")}")
            print(f"\t{sch.get("departure")} - {sch.get("arrival")}")
            print()
            counter += 1

    def run(self):
        while True:
            Application.show_menu()

            user_input = int(input())

            if user_input == 1:
                self.__show_schedule(self.__get_schedule())


            elif user_input == 3:
                break
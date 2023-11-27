class Transport:
    def way_to_travel(self):
        pass
# All info by template: "A-B": (time, fee),
# where time in hours, fee in BYN


class Plane(Transport):
    info = {
        "Минск-Варшава": (2, 300),
        "Минск-Москва": (1.2, 200),
        "Минск-Талин": (2.3, 700),
        "Минск-Вильнюс": (1, 200),
        "Минск-Берлин": (10, 1500)
    }

    def way_to_travel(self):
        print("Полёт")


class Train(Transport):
    info = {
        "Минск-Варшава": (8, 90),
        "Минск-Москва": (7, 30),
        "Минск-Талин": (10.0, 100),
        "Минск-Вильнюс": (6, 80),
        "Минск-Берлин": (36, 150)
    }

    def way_to_travel(self):
        print("Передвижение по рельсам")


class Car(Transport):
    info = {
        "Минск-Варшава": (12, 60),
        "Минск-Москва": (6.0, 45),
        "Минск-Талин": (17, 85),
        "Минск-Вильнюс": (12, 60),
        "Минск-Берлин": (45, 105)
    }

    def way_to_travel(self):
        print("Передвижение по дорогам")


def exercise_1() -> None:
    while True:
        trip_choice = choose_trip_route()
        if trip_choice == 0:
            break
        str_trip = convert_int_choice(trip_choice)
        process(str_trip)


def choose_trip_route() -> int:
    print("Выберите маршрут:\n"
          "1. Минск-Варшава\n"
          "2. Минск-Москва\n"
          "3. Минск-Талин\n"
          "4. Минск-Вильнюс\n"
          "5. Минск-Берлин\n"
          "0. Выход\n"
          "Ввод: "
          )
    trip_route_num = int()
    while True:
        try:
            trip_route_num = int(input())
            break
        except (TypeError, ValueError):
            print("Данные введены неверно, повторите попытку: ")
            continue
    return trip_route_num


def convert_int_choice(to_convert: int) -> str:
    if to_convert == 1:
        return "Минск-Варшава"
    elif to_convert == 2:
        return "Минск-Москва"
    elif to_convert == 3:
        return "Минск-Талин"
    elif to_convert == 4:
        return "Минск-Вильнюс"
    elif to_convert == 5:
        return "Минск-Берлин"


def process(str_trip: str) -> None:
    by_train = f"Поездом: {transport.Train.info[str_trip][0]} часов, {transport.Train.info[str_trip][1]} рублей\n"
    by_plane = f"Самолётом: {transport.Plane.info[str_trip][0]} часов, {transport.Plane.info[str_trip][1]} рублей\n"
    by_car = f"Автомобилем: {transport.Car.info[str_trip][0]} часов, {transport.Car.info[str_trip][1]} рублей\n"
    print(f"Возможные варианты маршрута \"{str_trip}\":\n"
          f"{by_train}"
          f"{by_plane}"
          f"{by_car}"
          )
    most_economical = compare_tuples(str_trip)
    print("Наиболее экономичный маршрут:\n")
    if most_economical == 1:
        print(by_train)
    elif most_economical == 2:
        print(by_car)
    elif most_economical == 3:
        print(by_plane)


def compare_tuples(trip: str) -> int:
    if (transport.Train.info[trip][1] / transport.Train.info[trip][0] < transport.Car.info[trip][1] / transport.Car.info[trip][0]
            and transport.Train.info[trip][1] / transport.Train.info[trip][0] < transport.Plane.info[trip][1] / transport.Plane.info[trip][0]):
        return 1
    if (transport.Car.info[trip][1] / transport.Car.info[trip][0] < transport.Train.info[trip][1] / transport.Train.info[trip][0]
            and transport.Car.info[trip][1] / transport.Car.info[trip][0] < transport.Plane.info[trip][1] / transport.Plane.info[trip][0]):
        return 2
    if (transport.Plane.info[trip][1] / transport.Plane.info[trip][0] < transport.Car.info[trip][1] / transport.Car.info[trip][0]
            and transport.Plane.info[trip][1] / transport.Plane.info[trip][0] < transport.Train.info[trip][1] / transport.Train.info[trip][0]):
        return 3

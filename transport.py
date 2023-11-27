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

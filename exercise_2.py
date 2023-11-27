class Entity:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.square = float()

    def count_square(self):
        self.square = self.width * self.height
        return self.square


def show_needed_square(walls, doors, windows):
    all_square = 0
    for i in walls:
        all_square = all_square + i.count_square()
    windows_square = 0
    for i in windows:
        windows_square = windows_square + i.count_square()
    doors_square = 0
    for i in doors:
        doors_square = doors_square + i.count_square()
    print(f"Необходимо обклеить {all_square - windows_square - doors_square} метров квадратных\n")


def exercise_2() -> None:
    walls = list()
    doors = list()
    windows = list()
    while True:
        print("Меню:\n"
              "1. Добавить стену\n"
              "2. Добавить дверь\n"
              "3. Добавить окно\n"
              "4. Вычислить площадь для оклейки\n"
              "0. Выход\n"
              "Ввод: ")
        choice = int()
        while True:
            try:
                choice = int(input())
                break
            except (TypeError, ValueError):
                print("Неверный ввод, повторите попытку: ")
                continue

        if choice == 0:
            break
        elif choice == 4:
            show_needed_square(walls, doors, windows)
            continue

        entity = Entity(0, 0)
        while True:
            try:
                width = float(input("Введите ширину: "))
                height = float(input("Введите высоту: "))
                entity.width = width
                entity.height = height
                break
            except (TypeError, ValueError):
                print("Неверный ввод, повторите попытку: ")
                continue

        if choice == 1:
            walls.append(entity)
        elif choice == 2:
            doors.append(entity)
        elif choice == 3:
            windows.append(entity)

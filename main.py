import exercise_1
import exercise_2


def main() -> None:
    while True:
        print("""Лабораторная работа #4:
        1. Транспорт
        2. Площадь стены для оклейки
        3. 
        0. Выход""")
        choice = int()
        while True:
            try:
                choice = int(input("Ввод: "))
                break
            except (TypeError, ValueError):
                print("Неверный ввод, повторите попытку: ")
                continue
        if choice == 0:
            break
        elif choice == 1:
            exercise_1.exercise_1()
        elif choice == 2:
            exercise_2.exercise_2()


main()

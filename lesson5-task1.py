"""
Задание №1
Пользователь вводит целое число.
Выведите его строку-описание вида "отрицательное четное число", "нулевое число", "положительное нечетное число",
например, численным описанием числа 190 является строка "положительное четное число".
Если число не является четным - выведите сообщение "число не является четным"
"""


def describe_number(number):

    if number == 0:
        print("Нулевое число")
    elif number > 0:
        if number % 2 == 0:
            print("Положительное четное число")
        else:
            print("Положительное нечетное число")
    else:
        if number % 2 == 0:
            print("Отрицательное четное число")
        else:
            print("Отрицательное нечетное число")

    if number % 2 != 0:
        print("Число не является четным")


number = int(input("Введите целое число: "))
describe_number(number)

"""
Задание №2
Дано пятизначное целое число.
Напишите алгоритм, который возведёт количество десятков в степень количества единиц.
Затем умножит это число на количество сотен. И делит получившееся число на разность количества десятков тысяч и количества тысяч

Например, есть число 46275

Необходимо возвести 7 (десятки) в степень 5 (единицы), умножить получившееся число на 2 (сотни),
и разделить на разность между 4 (десятки тысяч) и 6 (тысячи) то есть (4-6)

В результате необходимо получить вещественное число. В нашем примере это будет: -16807.0
"""
def calculate_expression(number):
    units = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    tens_of_thousands = number // 10000
    ten_power_units = tens ** units
    result = (ten_power_units * hundreds) / (tens_of_thousands - thousands)
    return result


input_number = int(input("Введите целое пятизначное число: "))
result = calculate_expression(input_number)
print(result)
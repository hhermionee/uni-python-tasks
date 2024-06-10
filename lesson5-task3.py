"""
Задание №3
Два инвестора - Майкл и Иван хотят вложиться в стартап.
Фаундеры сказали, что минимальная сумма инвестиций - X долларов, больше инвестировать можно сколько угодно.
У Майкла A долларов, у Ивана B долларов.
Если оба могут вложиться - выведите 2, если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности,
но вместе им хватает - 1, если никто - 0.
"""


investments_amount = int(input("Введите минимальную сумму инвестиций X: "))
mike_money = int(input("У Майкла A долларов: "))
ivan_money = int(input("У Ивана B долларов: "))

if mike_money >= investments_amount and ivan_money >= investments_amount:
    print(2)
elif mike_money >= investments_amount:
    print("Mike")
elif ivan_money >= investments_amount:
    print("Ivan")
elif mike_money + ivan_money >= investments_amount:
    print(1)
else:
    print(0)

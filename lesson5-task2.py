"""
Задание №2
Дано слово из маленьких латинских букв.
Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
Для решения задачи создайте переменную и в неё положите слово с помощью input()
А также определите количество каждой из этих гласных букв
Если какой-то из перечисленных букв нет - Выведите False
"""


word = input("Введите слово из маленьких латинских букв: ")
vowels_freq = {'a': 0, 'e': 0, 'o': 0, 'u': 0}
vowel_count = 0

for char in word:
    for vowel in vowels_freq.keys():
        if char == vowel:
            vowel_count += 1
            vowels_freq[vowel] += 1
consonant_count = len(word) - vowel_count

print("Количество гласных:", vowel_count)
print("Количество согласных:", consonant_count)

for vowel in vowels_freq.keys():
    vowel_freq_count = vowels_freq[vowel] if vowels_freq[vowel] != 0 else False
    print("Количество гласных", vowel, "-", vowel_freq_count)

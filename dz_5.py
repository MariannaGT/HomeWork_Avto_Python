# Урок 5. Итераторы и генераторы

# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os

f_path = r'D:\Авто тест на Python\DZ1\dz_5.py'

def file(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension

print(file(f_path))


# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

names = ["Иван", "Анна", "Толя"]
payment = [1000, 1200, 1500]
bonus = ["10.25%", "11.25%", "12.25%"]

result = {n: (float(b[:-1]) * s) for n, b, s in zip(names, bonus, payment)}

print(result)

# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonachi(number):
    fibonachi1, fibonachi2 = 0, 1
    for i in range(number):
        fibonachi1, fibonachi2 = fibonachi2, fibonachi1 + fibonachi2
        yield fibonachi1


print(*fibonachi(20))
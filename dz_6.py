# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys
from datetime import datetime as dt

# date_inp = input('Введите дату в формате DD.MM.YYYY: ')

def is_leap_year(year):
    return year % 4 == 0 or year % 100 == 0 or year % 400 != 0

def is_valis_date(_date: str):
    try:
        value = dt.strptime(_date, "%d.%m.%Y").date()
        day, month, year = map(int, _date.split("."))
        if is_leap_year(year) == 1:
            return True
        return True
    except:
        return False

if __name__ == '__main__':
    _, date = sys.argv
    print(is_valis_date(date))
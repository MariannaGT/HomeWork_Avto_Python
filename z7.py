# Урок 7. Файлы и файловая система

# Задача с семинара: ✔Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
# ✔Каждая группа включает файлы с несколькими расширениями. ✔В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os

DCT = {'Видео': ('mkv', 'avi', 'mp4'),
       'Изображение' : ('png', 'jpg', 'jpeg'),
       'Текст': ('txt', 'bin')}

def group(dir_):
    files = [file for file in os.listdir() if os.path.isfile(file)]
    for fold, exts in DCT.items():
        if fold not in os.listdir():
            os.mkdir(fold)
        for file in files:
            if file.split('.')[1] in exts:
               # os.replace(file, fold + '\\' + file)
                os.replace(file, os.path.join(os.getcwd(), fold, file))

if __name__ == '__main__':
    group(os.getcwd())
    
    
# 2. Напишите функцию группового переименования файлов. Она должна: ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер. ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога. ✔ принимать параметр расширение конечного файла. 
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 

from os import chdir, getcwd, listdir, mkdir
from pathlib import Path


__all__ = ['refactor_file']


def refactor_file(new_name: str,
                  old_ext: str, new_ext: str = None,
                  count_digits: int = 3,
                  range_name: range = (3, 6),
                  directory: str | Path = "test_dir"):
    if directory not in listdir():
        mkdir(directory)
    directory = getcwd() + '\\' + directory + '\\'
    chdir(directory)
    count = 1
    if new_ext is None:
        new_ext = old_ext
    for file in Path(getcwd()).iterdir():
        if file.is_file() and file.suffix == old_ext:
            new_file_name = f"{file.stem[range_name[0]:range_name[1]]}{new_name}_{count:0{count_digits}}{new_ext}"
            count += 1
            file.replace(new_file_name)
    if count > 1:
        print(f"Переименовано {count} файл(ов) {{old_ext}} в {{new_ext}}")
    else:
        print(f"Файлов с расширением {{old_ext}} не существует!")


refactor_file("_видео", old_ext=".txt", new_ext=".jpg")


if __name__ == '__main__':
    refactor_file("_видео", old_ext=".txt", new_ext=".jpg")
    

# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
print('See "__init__.py" file in dz_7')
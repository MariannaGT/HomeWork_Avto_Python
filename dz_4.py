
# Напишите функцию для транспонирования матрицы

matrix = [[7, 8, 9], 
          [4, 5, 6], 
          [3, 2, 1]]

new_matrix = list(map(list, zip(*matrix)))

print(new_matrix)

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


import collections.abc

def reverse_items(**kwargs):
    res_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, collections.abc.Hashable):
            res_dict[value] = key
        else:
            res_dict[str(value)] = key
    return res_dict

rev_dict = reverse_items(joint=50, Hello=8.0, Str='World', lst=[5, 4, 3], set_item={1,2,7,9, 'list'})
print(rev_dict)
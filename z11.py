# Урок 11. ООП. Особенности Python
# Решить задания, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

import numpy as np


class Matrix:
  
    def __init__(self, row: int,
                 column: int,
                 start: int = 0):
        self.row = row
        self.column = column
        self.start = start
        self.stop = start + (row * column)
        self.mat = np.arange(self.start, self.stop).reshape(self.row, self.column)

    def __str__(self):
        return str(self.mat)

    def __add__(self, other):
        if len(self.mat) != len(other.mat) or len(self.mat[0]) != len(other.mat[0]):
            raise ValueError("Матрицы должны быть одного размера")
        result = []
        for i in range(len(self.mat)):
            result.append([])
            for j in range(len(self.mat[0])):
                result[i].append(self.mat[i][j] + other.mat[i][j])
        return np.array(result)

    def __sub__(self, other):
        if len(self.mat) != len(other.mat) or len(self.mat[0]) != len(other.mat[0]):
            raise ValueError("Матрицы должны быть одного размера")
        result = []
        for i in range(len(self.mat)):
            result.append([])
            for j in range(len(self.mat[0])):
                result[i].append(self.mat[i][j] - other.mat[i][j])
        return np.array(result)

    def __mul__(self, other):
        if len(self.mat[0]) != len(other.mat):
            raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы")
        result = []
        for i in range(len(self.mat)):
            result.append([])
            for j in range(len(self.mat[0])):
                sum_ = 0
                for k in range(len(self.mat[0])):
                    sum_ += self.mat[i][k] * other.mat[k][j]
                    result[i].append(sum_)
        return np.array(result)


m1 = Matrix(4, 4, 2)
print(m1)
print(type(m1))
print()

m2 = Matrix(4, 4, 3)
print(m2)
print()

m3 = m1 - m2
print(m3)
print()

m4 = m1 * m2
print(m4)
print(type(m4))
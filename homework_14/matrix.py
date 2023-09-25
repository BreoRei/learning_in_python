import numpy as np


class Matrix:
    def __init__(self, matrix_values):
        self.matrix_values = matrix_values
    def __repr__(self):
        return f'Matrix({self.matrix_values})'
    def __str__(self):
        return f'матрица = {self.matrix_values}'
    def __add__(self, other):
        return Matrix(np.array(self.matrix_values) + np.array(other.matrix_values))
    def __mul__(self, other):
        return Matrix(np.array(self.matrix_values).dot(np.array(other.matrix_values)))
    def __eq__(self, other):
        return self.matrix_values == other.matrix_values
    def __gt__(self, other):
        return self.matrix_values > other.matrix_values
    def __lt__(self, other):
        return self.matrix_values < other.matrix_values


if __name__ == '__main__':
    arr = [[1, 2, 4, 2],
           [3, 4, 5, 1],
           [7, 8, 6, 4],
           [2, 4, 9, 1]]
    arr1 = [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]

    m = Matrix(arr)
    m1 = Matrix(arr1)
    m2 = Matrix(arr1)
    print(f'{m = }')
    print(m)

    print('Сравнение:')
    print(f'{m = } == {m2 = }: {m == m2}')
    print(f'{m1 = } == {m2 = }: {m1 == m2}')
    print(f'{m = } < {m2 = }: {m < m2}')
    print(f'{m1 = } < {m2 = }: {m1 < m2}')
    print(f'{m = } > {m2 = }: {m > m2}')
    print(f'{m1 = } > {m2 = }: {m1 > m2}')

    print('Сложение:')
    print(f'{m1 + m2 = }')

    print('Умножение:')
    print(f'{m * m2 = }')
    print(f'{m1 * m2 = }')


def matrix_test():
    """Функция тестирования матриц
    >>> from matrix import Matrix
    >>> m1 = Matrix([[1, 2, 4, 2], [3, 4, 5, 1], [7, 8, 6, 4], [2, 4, 9, 1]])
    >>> m2 = Matrix([[1, 2, 4, 2], [3, 4, 5, 1], [7, 8, 6, 4], [2, 4, 9, 1]])
    >>> m3 = Matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
    >>> m1 == m2
    True
    >>> m1 == m3
    False
    >>> m1 < m3
    False
    >>> m1 + m2
    Matrix([[ 2  4  8  4]
     [ 6  8 10  2]
     [14 16 12  8]
     [ 4  8 18  2]])
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

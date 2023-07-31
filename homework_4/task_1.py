import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(func.__doc__)
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time:.10f} секунд")
        return result
    return wrapper


@timing_decorator
def matrix_transposition(matrix=None) -> list[list[int]]:
    """Tранспонирование матрицы"""
    if matrix is None:
        matrix = [[1, 2, 3], [4, 5, 6]]
    new_matrix = []
    inner_lst = []
    for row_number in range(len(matrix)):
        for num, item in enumerate(matrix[row_number]):
            if row_number == 0:
                inner_lst.append(item)
                new_matrix.append(inner_lst)
                inner_lst = []
            else:
                new_matrix[num].append(item)
    return new_matrix


@timing_decorator
def matrix_transposition_fast(matrix=None) -> list[list[int]]:
    """Tранспонирование матрицы"""
    if matrix is None:
        matrix = [[1, 2, 3], [4, 5, 6]]
    new_matrix = []
    for first_row_value, second_row_value in zip(matrix[0], matrix[1]):
        new_matrix.append([first_row_value, second_row_value])
    return new_matrix


if __name__ == '__main__':
    print(matrix_transposition())
    print()
    print(matrix_transposition_fast())

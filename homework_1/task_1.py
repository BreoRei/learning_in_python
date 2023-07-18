from typing import Callable, Any


def decorator(headline_messeg, end_messeg) -> Callable:

    def func_decorator(func: Callable) -> Callable:
        print(headline_messeg)

        def wrapper(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)
            print(end_messeg)
            return result

        return wrapper

    return func_decorator


def convert_to_numbers(str_list: list[str]) -> list[float]:
    return [float(i) for i in str_list]


def what_is_this_triangle(num_list: list[float]) -> None:
    if triangle_whether(num_list):
        if num_list[0] == num_list[1] == num_list[2]:
            print("Это равносторонний треугольник!")
        elif num_list[0] == num_list[1] or num_list[0] == num_list[2] or num_list[1] == num_list[2]:
            print("Это равнобедренный треугольник!")
        else:
            print("Это разносторонний треугольник!")
    else:
        print("Это не треугольник!")


def triangle_whether(num_list: list[float]) -> bool:
    checkbox: bool = True
    if num_list[0] >= num_list[1] + num_list[2]:
        checkbox = False
    elif num_list[1] >= num_list[0] + num_list[2]:
        checkbox = False
    elif num_list[2] >= num_list[0] + num_list[1]:
        checkbox = False
    return checkbox


@decorator("Начало работы.", "Завершение работы.")
def get_side_values():
    NUMBER_OF_PARTIES = 3
    try:
        data: list[str] = input("Введите три стороны треугольника через пробел --> ").split()
        if len(data) > NUMBER_OF_PARTIES:
            print("Вы ввели больше трёх значений!")
        elif len(data) < NUMBER_OF_PARTIES:
            print("Вы ввели меньше трёх значений!")
        else:
            triangle_sides: list[float] = convert_to_numbers(str_list=data)
            what_is_this_triangle(num_list=triangle_sides)
    except ValueError as e:
        print("Ошибка при преобразовании строки в число:", e)


if __name__ == '__main__':
    get_side_values()

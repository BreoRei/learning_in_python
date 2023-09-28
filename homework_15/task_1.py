import logging
from functools import wraps
import argparse


NUMBER_OF_PARTIES = 3
FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" '\
         'в строке {lineno:03d} функция "{funcName}()" '\
         'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(format=FORMAT,
                    style='{',
                    filename='task_log.log',
                    encoding='utf-8',
                    level=logging.ERROR)


logging = logging.getLogger(__name__)


def deco(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f'Функция {func.__name__} с аргументами {args=}, {kwargs} выдала ошибку {e}')

    return wrapper


def convert_to_numbers(str_list: list[str]) -> list[float]:
    return [float(i) for i in str_list]


def what_is_this_triangle(num_list: list[float]) -> str:
    if triangle_whether(num_list):
        if num_list[0] == num_list[1] == num_list[2]:
            return "Это равносторонний треугольник!"
        elif num_list[0] == num_list[1] or num_list[0] == num_list[2] or num_list[1] == num_list[2]:
            return "Это равнобедренный треугольник!"
        else:
            return "Это разносторонний треугольник!"
    else:
        return "Это не треугольник!"


def triangle_whether(num_list: list[float]) -> bool:
    checkbox: bool = True
    if num_list[0] >= num_list[1] + num_list[2]:
        checkbox = False
    elif num_list[1] >= num_list[0] + num_list[2]:
        checkbox = False
    elif num_list[2] >= num_list[0] + num_list[1]:
        checkbox = False
    return checkbox


@deco
def get_side_values(value):
    data: list[str] = value.split()
    if len(data) > NUMBER_OF_PARTIES:
        raise ValueError("Вы ввели больше трёх значений!")
    elif len(data) < NUMBER_OF_PARTIES:
        raise ValueError("Вы ввели меньше трёх значений!")
    else:
        triangle_sides: list[float] = convert_to_numbers(str_list=data)
        return what_is_this_triangle(num_list=triangle_sides)


def create_pars():
    parser = argparse.ArgumentParser(description='triangle sides parser')
    parser.add_argument('-s', '--sides', type=str)
    args = parser.parse_args()
    return get_side_values(f'{args.sides}')


if __name__ == '__main__':
    print(create_pars())
    # get_side_values("2 4 g")

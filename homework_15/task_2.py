import logging
from functools import wraps
import argparse


MINIMUM_VALUE = 1
MAXIMUM_VALUE = 100000
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


def get_number(number: int) -> int:
    if MINIMUM_VALUE < number < MAXIMUM_VALUE:
        return number
    elif number == MINIMUM_VALUE:
        raise ValueError("Число 1 — не является ни простым, ни составным числом.")
    else:
        raise ValueError("Вы ввели неверное число.")


def is_it_simple_number(number) -> str:
    for i in range(2, number):
        if number % i == 0:
            return f"Число {number} составное"
    else:
        return f"Число {number} простое"


@deco
def program(value: str) -> str:
    convert_value = int(value)
    number = get_number(convert_value)
    result = is_it_simple_number(number)
    return result


def create_pars():
    parser = argparse.ArgumentParser(description='checking prime or composite number')
    parser.add_argument('-n', '--number', type=int)
    args = parser.parse_args()
    return program(f'{args.number}')


if __name__ == '__main__':
    print(create_pars())

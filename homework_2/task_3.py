from fractions import Fraction
from math import gcd


def work_with_fractions() -> None:
    try:
        first_fraction = input("Введите первую дробь вида 1/1 -> ")
        second_fraction = input("Введите вторую дробь вида 1/1 -> ")
        first_numer, first_den = map(int, first_fraction.split("/"))
        second_numer, second_den = map(int, second_fraction.split("/"))
        sum_fract = get_sum(first_numer, first_den, second_numer, second_den)
        multiplication_fract = get_multiplication(first_numer, first_den, second_numer, second_den)
        print(f'Сумма дробей: {sum_fract}\n'
              f'Произведение: {multiplication_fract}')
        print(f'Проверка с помощью fractions:\n'
              f'Сумма дробей: {Fraction(first_numer, first_den) + Fraction(second_numer, second_den)}\n'
              f'Произведение: {Fraction(first_numer, first_den) * Fraction(second_numer, second_den)}')
    except ValueError:
        print("Ошибка. Это не число.")


def get_sum(first_numer, first_den, second_numer, second_den) -> str:
    sum_numer = (first_numer * second_den) + (second_numer * first_den)
    sum_den = first_den * second_den
    gcd_value = gcd(sum_numer, sum_den)
    sum_numer //= gcd_value
    sum_den //= gcd_value
    return f'{sum_numer}/{sum_den}'


def get_multiplication(first_numer, first_den, second_numer, second_den) -> str:
    multiplication_numer = first_numer * second_numer
    multiplication_den = first_den * second_den
    gcd_value = gcd(multiplication_numer, multiplication_den)
    multiplication_numer //= gcd_value
    multiplication_den //= gcd_value
    return f'{multiplication_numer}/{multiplication_den}'


if __name__ == '__main__':
    work_with_fractions()

def get_number() -> int:
    MINIMUM_VALUE = 1
    MAXIMUM_VALUE = 100000
    try:
        number: int = int(input("Введите число от 1 до 100.000 --> "))
        if MINIMUM_VALUE < number < MAXIMUM_VALUE:
            return number
        elif number == 1:
            print("Число 1 — не является ни простым, ни составным числом.")
        else:
            print("Вы ввели неверное число.")
    except ValueError:
        print("Это не число!")
    exit()


def is_it_simple_number(number) -> None:
    if number == 2:
        print("Число простое")
    else:
        for i in range(2, number):
            if number % i == 0:
                print("Число составное")
                break
        else:
            print("Число простое")


def program() -> None:
    number = get_number()
    is_it_simple_number(number)


if __name__ == '__main__':
    program()

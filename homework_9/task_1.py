import csv
import json
from random import randint


def random_numbers():
    while True:
        num = randint(-10, 10)
        if num != 0:
            yield num


def save_to_json(func):

    def wrapper(*args, **kwargs):
        data = {}
        try:
            with open('param_and_result.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            pass
        finally:
            with open('param_and_result.json', 'w', encoding='utf-8') as f:
                result = func(*args, **kwargs)
                data[str(args)] = result
                json.dump(data, f, indent=4)

        return func

    return wrapper


def substitute_numbers(func):

    def wrapper():

        with open('number_of_lines_from_100_to_1000.csv', 'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                if len(row) == 3:
                    a, b, c = map(float, row)
                    func(a, b, c)
                else:
                    pass
                    print(f"Invalid row: {row}")

    return wrapper


@substitute_numbers
@save_to_json
def equation_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = round((-b + d ** 0.5) / (2 * a), 2)
        x2 = round((-b - d ** 0.5) / (2 * a), 2)
        return [x1, x2]
    elif d == 0:
        x1 = round((-b + d ** 0.5) / (2 * a), 2)
        return [x1]
    else:
        return [None]


def create_file_with_3_numbers_per_line_from_100_to_1000_lines():
    data = []
    rnd = randint(100, 1000)
    with open('number_of_lines_from_100_to_1000.csv', 'w', encoding='utf-8', newline="") as f:
        writer = csv.writer(f, delimiter=' ')
        generator = random_numbers()
        for _ in range(rnd):
            num = [next(generator) for _ in range(3)]
            data.append(num)
        writer.writerows(data)
    equation_roots()


if __name__ == '__main__':
    create_file_with_3_numbers_per_line_from_100_to_1000_lines()


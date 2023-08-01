from typing import Generator


def print_fibonacci(func):
    def wrapper(*args, **kwargs):
        fibonacci_generator = func(*args, **kwargs)
        output = []

        for number, fibo in enumerate(fibonacci_generator):
            output.append(fibo)
            print(f'fib:{number:<4} {fibo}')

        return output

    return wrapper


@print_fibonacci
def fib(n) -> Generator[int, int, None]:
    a, b = 0, 1
    for _ in range(n+1):
        yield a
        a, b = b, a + b


def fibonacci_gen() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    fib(10)
    print()

    fib_gen = fibonacci_gen()
    print(next(fib_gen))
    print(next(fib_gen))
    print(next(fib_gen))
    print(next(fib_gen))
    print(next(fib_gen))

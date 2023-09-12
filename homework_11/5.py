class Rectangle:
    """Класс имеет методы сложения(__add__), вычитания(__sub__),
поиск площади(calc_square) и поиск периметра(calc_perimeter)"""
    def __init__(self, length_cm: float, width_cm: float = None) -> None:
        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm

    def calc_perimeter(self):
        return (self.width + self.length) * 2

    def calc_square(self):
        return self.width * self.length

    def __add__(self, other):
        return Rectangle(length_cm=(self.length + other.length), width_cm=self.width)

    def __sub__(self, other):
        return Rectangle(length_cm=(self.length - other.length), width_cm=self.width)

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'

    def __str__(self):
        return (f'Длинна: {self.length}, ширина: {self.width}, '
                f'S={self.calc_square()}, P={self.calc_perimeter()}')


if __name__ == '__main__':
    r1 = Rectangle(length_cm=4)
    print(r1.calc_perimeter())
    r2 = Rectangle(length_cm=4, width_cm=5)
    print(r2.calc_perimeter())
    r3 = r2 + r1
    print(r3.calc_perimeter())

    print(f'{r2 = }')
    print(f'{r3 = }')
    print(r3)
    print(r3.__doc__)

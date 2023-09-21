class BasicException(Exception):
    pass


class BasicExceptionNegativeValue(BasicException):
    def __str__(self):
        return 'Значение должно быть больше 0'


class Rectangle:
    def __init__(self, length_cm: float, width_cm: float = None) -> None:
        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, other):
        if other < 0:
            raise BasicExceptionNegativeValue
        self.__length = other

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, other):
        if other < 0:
            raise BasicExceptionNegativeValue
        self.__width = other


if __name__ == '__main__':
    r = Rectangle(length_cm=2, width_cm=3)
    print(r.length)
    print(r.width)
    r.length = 2
    print(r.length)
    print(r.width)
    r.length = -1
    print(r.length)
    print(r.width)

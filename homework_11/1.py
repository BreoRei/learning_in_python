import time


class MyStr(str):
    """Создает класс наследуемый от str с Иминем автора, значением, и временем создания."""
    def __new__(cls, value: str, name: str):
        instance = super().__new__(cls, value)
        instance.value = value
        instance.name = name
        instance.time = time.time()
        return instance

    def __repr__(self):
        return f'MyStr({self.value}, {self.name})'

    def __str__(self):
        return (f'Имя автора: {self.name}, время создания: {self.time},\n'
                f'текст: {self.value}')


if __name__ == '__main__':
    s = MyStr('ffwgerh3tsdgsfw4ee', 'Пушкин')
    print(s)
    print(s.name)
    print(s.time)
    print(repr(s))
    print(f'{s = }')
    print(s.__doc__)

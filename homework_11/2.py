class Archive:
    """Создайте класс Архив, который хранит пару свойств число и строку.
При создании экземпляра класса, старые данные сохраняются в пару списков."""
    archive = None

    def __new__(cls, *args, **kwargs):
        if cls.archive:
            cls.archive.old_text.append(cls.archive.text)
            cls.archive.old_num.append(cls.archive.num)
        else:
            cls.archive = super().__new__(cls)
            cls.archive.old_text = []
            cls.archive.old_num = []
        return cls.archive

    def __init__(self, num: int, text: str):
        self.num = num
        self.text = text

    def __repr__(self):
        return f'Archive({self.num}, {self.text})'

    def __str__(self):
        return (f'Число: {self.num}, строка: {self.text},\n'
                f'архив чисел: {self.old_num}\n'
                f'архив строк: {self.old_text}')


if __name__ == '__main__':
    a = Archive(3, '2333')
    b = Archive(4, '453')
    c = Archive(5, 'dsfd')
    print(c.old_num, c.old_text)

    print(f'{c = }')
    print(a)
    print(b.__doc__)




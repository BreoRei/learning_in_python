def rev_kwargs(**kwargs) -> dict[str | int: str]:
    """
    Функцию принимает на вход только ключевые параметры и возвращает словарь.
    Если ключ не хешируем, используйте его строковое представление.
    :param kwargs: res=1, reverse=[1, 2, 3]
    :return: {1: 'res', '[1, 2, 3]': 'reverse'}
    """
    inner_dict = {}
    for key, value in kwargs.items():
        try:
            if hash(value):
                inner_dict[value] = key
        except TypeError:
            inner_dict[str(value)] = key
    return inner_dict


if __name__ == '__main__':
    print(rev_kwargs(res=1, reverse=[1, 2, 3]))

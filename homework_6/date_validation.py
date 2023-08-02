from sys import argv
from datetime import datetime

MONTH = {'1': 'января',
         '2': 'февраля',
         '3': 'марта',
         '4': 'апреля',
         '5': 'мая',
         '6': 'июня',
         '7': 'июля',
         '8': 'августа',
         '9': 'сентября',
         '10': 'октября',
         '11': 'ноября',
         '12': 'декабря'}


def check():
    value, *_ = argv[1:]
    lst_date = value.split('.')
    if len(lst_date) == 3:
        try:
            datetime.strptime(value, '%d.%m.%Y')
            print(f'Верный формат даты:\n{lst_date[0]} {MONTH.get(lst_date[1])} {lst_date[2]}')
        except Exception:
            print('Неверный формат даты')
    elif len(lst_date) == 2:
        try:
            datetime.strptime(value, '%d.%m')
            print(f'Верный формат даты:\n{lst_date[0]} {MONTH.get(lst_date[1])}')
        except Exception:
            print('Неверный формат даты')
    else:
        print('Неверный формат даты')


if __name__ == '__main__':
    check()

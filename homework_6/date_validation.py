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

START_GREGORIAN_CALENDAR = 1
STOP_GREGORIAN_CALENDAR = 10000


def check():
    value = argv[1:]
    if len(value) == 1:
        try:
            day, monyh, year = value[0].split('.')
            datetime.strptime(f'{day}.{monyh}', '%d.%m')
            if START_GREGORIAN_CALENDAR <= int(year) < STOP_GREGORIAN_CALENDAR:
                print(f'Верный формат даты:\n{day} {MONTH.get(monyh)} {year}')
                return True
            else:
                print('Неверный формат даты')
        except Exception:
            print('Неверный формат даты')
    else:
        print('Неверный формат даты')
    return False


if __name__ == '__main__':
    check()

NAME = ['Иван', 'Николай', 'Олег', 'Евгений']
RATE = [21000, 23500, 28600, 25300]
AWARD = ['9.25%', '10.31%', '7.3%', '8%']


def get_premium_value(name=None, rate=None, award=None):
    if award is None:
        award = AWARD
    if rate is None:
        rate = RATE
    if name is None:
        name = NAME
    result = {n: round(r * (float(a[:-1]) / 100), 2) for n, r, a in zip(name, rate, award)}
    return result


if __name__ == '__main__':
    bonus = get_premium_value()
    print(bonus)

_initial_share_price: dict[str: float] = {}


def print_txt(txt):
    def inner_func(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f'{txt}{result}')
            return result
        return wrapper
    return inner_func


@print_txt('Цена портфеля: ')
def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    global _initial_share_price
    _initial_share_price = prices.copy()
    portfolio_sum: float = 0
    for key, value in stocks.items():
        portfolio_sum += value*prices.get(key)
    return round(portfolio_sum, 2)


@print_txt('Доходность портфеля в %: ')
def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return round((current_value - initial_value) / 100, 2)


@print_txt('Акция с самой большой прибылью: ')
def get_most_profitable_stock(prices: dict) -> str:
    maximum_profit: float = 0
    share_name: str = ''
    for key, value in prices.items():
        if (value - _initial_share_price[key]) > maximum_profit:
            maximum_profit = value - _initial_share_price[key]
            share_name = key
    return share_name


if __name__ == '__main__':
    stocks_1 = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices_1 = {"GOOGL": 2500.75, "MSFT": 300.50, "AAPL": 150.25}
    prices_2 = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}

    portfolio_price = calculate_portfolio_value(stocks=stocks_1,
                                                prices=prices_1)

    calculate_portfolio_return(initial_value=10000, current_value=15000)

    get_most_profitable_stock(prices=prices_2)

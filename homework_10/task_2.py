class StockPortfolio:
    def __init__(self):
        self.__stocks = {}

    def add_stock(self, name, *args):
        if len(args) == 1:
            share_name = self.__stocks.get(name)
            share_name['price_change'] = args[0]
        else:
            price, quantity = args
            if self.__stocks.get(name):
                result = self._average_price(name, price, quantity)
                self.__stocks[name] = result
            else:
                self.__stocks[name] = {
                        'price': price,
                        'quantity': quantity,
                        'price_change': price
                }

    def _average_price(self, name, price, quantity):
        share = self.__stocks.get(name)
        share_price = share.get('price')
        share_quantity = share.get('quantity')
        new_quantity = share_quantity + quantity
        new_price = round(((share_price * share_quantity) + (price * quantity)) / new_quantity, 2)
        share['price'] = new_price
        share['quantity'] = new_quantity
        share['price_change'] = new_price
        return share

    def get_most_profitable_stock(self):
        name = ''
        high_price = 0
        for key, stock in self.__stocks.items():
            current_price = stock['price'] - stock['price_change']
            if current_price > high_price:
                name = key
                high_price = current_price
        print(f'Акция с самым большим профитом     \n'
              f'Название: {name:10} Профит: {high_price:6}\n')
        return high_price

    def __share_price(self):
        total_price = 0
        for _, stock in self.__stocks.items():
            stock_value = stock['price'] * stock['quantity']
            total_price += stock_value
        return total_price

    def share_purchase_price(self):
        total_price_change = 0
        for _, stock in self.__stocks.items():
            stock_value = stock['price_change'] * stock['quantity']
            total_price_change += stock_value
        return total_price_change

    def portfolio_profit(self):
        total_price_change = self.share_purchase_price()
        total_price = self.__share_price()
        total_profit = total_price - total_price_change
        return total_profit

    def __str__(self):
        result = ""
        for key, value in self.__stocks.items():
            result += f'{key:10} {str(value)}\n'
        return result


if __name__ == '__main__':
    portfolio = StockPortfolio()

    portfolio.add_stock('Apple', 150, 10)
    portfolio.add_stock('Microsoft', 200, 5)
    portfolio.add_stock('Google', 300, 5)
    portfolio.add_stock('Microsoft', 451, 5)

    portfolio.add_stock('Apple', 120)
    portfolio.add_stock('Microsoft', 220)
    portfolio.add_stock('Google', 350)

    purchase_price = portfolio.share_purchase_price()
    portfolio_profit = portfolio.portfolio_profit()
    print(f'{purchase_price=}')
    print(f'{portfolio_profit=}')
    print(portfolio)

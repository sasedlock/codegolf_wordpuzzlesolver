# Example of how to use the Observable and Observer abstract classes

from observable import Observable
from observer import Observer


class AmericanStockMarket(Observer):
    def update(self, *args, **kwargs):
        print("American stock market received: {0}\n{1}".format(args[0], kwargs))


class JapaneseStockMarket(Observer):
    def update(self, *args, **kwargs):
        print("Japanese stock market received: {0}\n{1}".format(args, kwargs))

if __name__ == "__main__":
    observable = Observable()

    american_observer = AmericanStockMarket()
    observable.register(american_observer)

    japanese_observer = JapaneseStockMarket()
    observable.register(japanese_observer)

    observable.update_observers('Market Rally', 'Hello World')


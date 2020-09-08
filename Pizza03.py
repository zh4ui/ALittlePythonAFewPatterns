"""
>>> a = Anchovy(Olive(Anchovy(Cheese(Crust())))).removeAnchovy()
>>> whatPizza(a)
Olive/Cheese/Crust/

>>> b = Olive(Anchovy(Cheese(Anchovy(Crust())))).removeAnchovy().topAnchovyWithCheese()
>>> whatPizza(b)
Olive/Cheese/Crust/

>>> c = Spinach(Anchovy(Crust())).substituteAnchovyByCheese()
>>> whatPizza(c)
Spinach/Cheese/Crust/
"""


from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def removeAnchovy(self) -> "Pizza":
        pass

    @abstractmethod
    def topAnchovyWithCheese(self) -> "Pizza":
        pass

    @abstractmethod
    def substituteAnchovyByCheese(self) -> "Pizza":
        pass


class Crust(Pizza):
    def removeAnchovy(self) -> Pizza:
        return Crust()

    def topAnchovyWithCheese(self) -> Pizza:
        return Crust()

    def substituteAnchovyByCheese(self) -> Pizza:
        return Crust()


class Cheese(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def removeAnchovy(self) -> Pizza:
        return Cheese(self.pizza.removeAnchovy())

    def topAnchovyWithCheese(self) -> Pizza:
        return Cheese(self.pizza.topAnchovyWithCheese())

    def substituteAnchovyByCheese(self) -> Pizza:
        return Cheese(self.pizza.substituteAnchovyByCheese())


class Olive(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def removeAnchovy(self) -> Pizza:
        return Olive(self.pizza.removeAnchovy())

    def topAnchovyWithCheese(self) -> Pizza:
        return Olive(self.pizza.topAnchovyWithCheese())

    def substituteAnchovyByCheese(self) -> Pizza:
        return Olive(self.pizza.substituteAnchovyByCheese())


class Anchovy(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def removeAnchovy(self) -> Pizza:
        return self.pizza.removeAnchovy()

    def topAnchovyWithCheese(self) -> Pizza:
        return Cheese(Anchovy(self.pizza.topAnchovyWithCheese()))

    def substituteAnchovyByCheese(self) -> Pizza:
        return Cheese(self.pizza.substituteAnchovyByCheese())


class Sausage(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def removeAnchovy(self) -> Pizza:
        return Sausage(self.pizza.removeAnchovy())

    def topAnchovyWithCheese(self) -> Pizza:
        return Sausage(self.pizza.topAnchovyWithCheese())

    def substituteAnchovyByCheese(self) -> Pizza:
        return Sausage(self.pizza.substituteAnchovyByCheese())


class Spinach(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def removeAnchovy(self) -> Pizza:
        return Spinach(self.pizza.removeAnchovy())

    def topAnchovyWithCheese(self) -> Pizza:
        return Spinach(self.pizza.topAnchovyWithCheese())

    def substituteAnchovyByCheese(self) -> Pizza:
        return Spinach(self.pizza.substituteAnchovyByCheese())


def whatPizza(pizza):
    print(pizza.__class__.__name__, end="/")
    if hasattr(pizza, "pizza"):
        whatPizza(pizza.pizza)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

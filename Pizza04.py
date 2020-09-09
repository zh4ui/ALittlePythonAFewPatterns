"""
>>> a = Anchovy(Olive(Anchovy(Cheese(Crust())))).removeAnchovy()
>>> whatPizza(a)
Olive/Cheese/Crust/

>>> b = Olive(Anchovy(Cheese(Anchovy(Crust())))).removeAnchovy().topAnchovyWithCheese()
>>> whatPizza(b)
Olive/Cheese/Crust/

"""


from abc import ABC, abstractmethod


class RemoveAnchovy(object):
    def forCrust(self):
        return Crust()

    def forCheese(self, pizza: "Pizza"):
        return Cheese(pizza.removeAnchovy())

    def forOlive(self, pizza: "Pizza"):
        return Olive(pizza.removeAnchovy())

    def forAnchovy(self, pizza: "Pizza"):
        return pizza.removeAnchovy()

    def forSausage(self, pizza: "Pizza"):
        return Sausage(pizza.removeAnchovy())


class TopAnchovyWithCheese(object):
    def forCrust(self):
        return Crust()

    def forCheese(self, pizza: "Pizza"):
        return Cheese(pizza.topAnchovyWithCheese())

    def forOlive(self, pizza: "Pizza"):
        return Olive(pizza.topAnchovyWithCheese())

    def forAnchovy(self, pizza: "Pizza"):
        return Cheese(Anchovy(pizza.topAnchovyWithCheese()))

    def forSausage(self, pizza: "Pizza"):
        return Sausage(pizza.topAnchovyWithCheese())


class SubstituteAnchovyByCheese(object):
    def forCrust(self):
        return Crust()

    def forCheese(self, pizza: "Pizza"):
        return Cheese(pizza.substituteAnchovyByCheese())

    def forOlive(self, pizza: "Pizza"):
        return Olive(pizza.substituteAnchovyByCheese())

    def forAnchovy(self, pizza: "Pizza"):
        return Cheese(pizza.substituteAnchovyByCheese())

    def forSausage(self, pizza: "Pizza"):
        return Sausage(pizza.substituteAnchovyByCheese())


class Pizza(ABC):

    removeAnchovyFn = RemoveAnchovy()
    topAnchovyWithCheeseFn = TopAnchovyWithCheese()
    substituteAnchovyByCheeseFn = SubstituteAnchovyByCheese()

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
        return self.removeAnchovyFn.forCrust()

    def topAnchovyWithCheese(self) -> Pizza:
        return self.topAnchovyWithCheeseFn.forCrust()

    def substituteAnchovyByCheese(self) -> Pizza:
        return self.substituteAnchovyByCheeseFn.forCrust()


class Cheese(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def removeAnchovy(self) -> Pizza:
        return self.removeAnchovyFn.forCheese(self.pizza)

    def topAnchovyWithCheese(self) -> Pizza:
        return self.topAnchovyWithCheeseFn.forCheese(self.pizza)

    def substituteAnchovyByCheese(self) -> Pizza:
        return self.substituteAnchovyByCheeseFn.forCheese(self.pizza)


class Olive(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def removeAnchovy(self) -> Pizza:
        return self.removeAnchovyFn.forOlive(self.pizza)

    def topAnchovyWithCheese(self) -> Pizza:
        return self.topAnchovyWithCheeseFn.forOlive(self.pizza)

    def substituteAnchovyByCheese(self) -> Pizza:
        return self.substituteAnchovyByCheeseFn.forOlive(self.pizza)


class Anchovy(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def removeAnchovy(self) -> Pizza:
        return self.removeAnchovyFn.forAnchovy(self.pizza)

    def topAnchovyWithCheese(self) -> Pizza:
        return self.topAnchovyWithCheeseFn.forAnchovy(self.pizza)

    def substituteAnchovyByCheese(self) -> Pizza:
        return self.substituteAnchovyByCheeseFn.forAnchovy(self.pizza)


class Sausage(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def removeAnchovy(self) -> Pizza:
        return self.removeAnchovyFn.forSausage(self.pizza)

    def topAnchovyWithCheese(self) -> Pizza:
        return self.topAnchovyWithCheeseFn.forSausage(self.pizza)

    def substituteAnchovyByCheese(self) -> Pizza:
        return self.substituteAnchovyByCheeseFn.forSausage(self.pizza)


def whatPizza(pizza):
    print(pizza.__class__.__name__, end="/")
    if hasattr(pizza, "pizza"):
        whatPizza(pizza.pizza)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

"""
>>> Skewer().onlyOnions()
True
>>> Onion(Onion(Skewer())).onlyOnions()
True
>>> Lamb(Skewer()).onlyOnions()
False
>>> Onion(Lamb(Skewer())).onlyOnions()
False
>>> isinstance(Tomato(Skewer()), Shish)
True
"""

from abc import ABC, abstractmethod


class OnlyOnions(object):
    def forSkewer(self):
        return True

    def forOnion(self, s: "Shish"):
        return s.onlyOnions()

    def forLamb(self, s: "Shish"):
        return False

    def forTomato(self, s: "Shish"):
        return False


class IsVegetarian(object):
    def forSkewer(self):
        return True

    def forOnion(self, s: "Shish"):
        return s.isVegetarian()

    def forLamb(self, s: "Shish"):
        return False

    def forTomato(self, s: "Shish"):
        return s.isVegetarian()


class Shish(ABC):
    onlyOnionsFn = OnlyOnions()
    isVegetarianFn = IsVegetarian()

    @abstractmethod
    def onlyOnions(self) -> bool:
        pass

    @abstractmethod
    def isVegetarian(self) -> bool:
        pass


class Skewer(Shish):
    def onlyOnions(self) -> bool:
        return self.onlyOnionsFn.forSkewer()

    def isVegetarian(self) -> bool:
        return self.isVegetarianFn.forSkewer()


class Onion(Shish):
    def __init__(self, shish: Shish):
        self.shish = shish

    def onlyOnions(self) -> bool:
        return self.onlyOnionsFn.forOnion(self.shish)

    def isVegetarian(self) -> bool:
        return self.isVegetarianFn.forOnion(self.shish)


class Lamb(Shish):
    def __init__(self, shish: Shish):
        self.shish = shish

    def onlyOnions(self) -> bool:
        return self.onlyOnionsFn.forLamb(self.shish)

    def isVegetarian(self) -> bool:
        return self.isVegetarianFn.forLamb(self.shish)


class Tomato(Shish):
    def __init__(self, shish: Shish):
        self.shish = shish

    def onlyOnions(self) -> bool:
        return self.onlyOnionsFn.forTomato(self.shish)

    def isVegetarian(self) -> bool:
        return self.isVegetarianFn.forTomato(self.shish)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

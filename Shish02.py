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


class Shish(ABC):
    @abstractmethod
    def onlyOnions(self) -> bool:
        pass

    @abstractmethod
    def isVegetarian(self) -> bool:
        pass


class Skewer(Shish):
    def onlyOnions(self) -> bool:
        return True

    def isVegetarian(self) -> bool:
        return True


class Onion(Shish):
    def __init__(self, shish: Shish):
        self.shish = shish

    def onlyOnions(self) -> bool:
        return self.shish.onlyOnions()

    def isVegetarian(self) -> bool:
        return self.shish.isVegetarian()


class Lamb(Shish):
    def __init__(self, shish: Shish):
        self.shish = shish

    def onlyOnions(self) -> bool:
        return False

    def isVegetarian(self) -> bool:
        return False


class Tomato(Shish):
    def __init__(self, shish: Shish):
        self.shish = shish

    def onlyOnions(self) -> bool:
        return False

    def isVegetarian(self) -> bool:
        return self.shish.isVegetarian()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

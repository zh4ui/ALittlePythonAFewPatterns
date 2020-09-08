"""
>>> isinstance(Shallot(Radish(Holder(Dagger()))), Kebab)
True
>>> isinstance(Shallot(Radish(Holder(Gold()))), Kebab)
True

>>> Shallot(Radish(Holder(Dagger()))).isVeggie()
True

>>> Shallot(Radish(Holder(int(5)))).isVeggie()
True

>>> Radish(Shallot(Shrimp(Holder(int(52))))).whatHolder()
52
"""


from abc import ABC, abstractmethod
from Rod02 import *
from Plate02 import *


class Kebab(ABC):
    @abstractmethod
    def isVeggie(self) -> bool:
        pass

    @abstractmethod
    def whatHolder(self):
        pass


class Holder(Kebab):
    def __init__(self, obj):
        self.obj = obj

    def isVeggie(self) -> bool:
        return True

    def whatHolder(self):
        return self.obj


class Shallot(Kebab):
    def __init__(self, kebab):
        self.kebab = kebab

    def isVeggie(self) -> bool:
        return self.kebab.isVeggie()

    def whatHolder(self):
        return self.kebab.whatHolder()


class Shrimp(Kebab):
    def __init__(self, kebab):
        self.kebab = kebab

    def isVeggie(self) -> bool:
        return False

    def whatHolder(self):
        return self.kebab.whatHolder()


class Radish(Kebab):
    def __init__(self, kebab):
        self.kebab = kebab

    def isVeggie(self) -> bool:
        return self.kebab.isVeggie()

    def whatHolder(self):
        return self.kebab.whatHolder()


class Pepper(Kebab):
    def __init__(self, kebab):
        self.kebab = kebab

    def isVeggie(self) -> bool:
        return self.kebab.isVeggie()

    def whatHolder(self):
        return self.kebab.whatHolder()


class Zucchini(Kebab):
    def __init__(self, kebab):
        self.kebab = kebab

    def isVeggie(self) -> bool:
        return self.kebab.isVeggie()

    def whatHolder(self):
        return self.kebab.whatHolder()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

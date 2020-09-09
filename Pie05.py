"""
>>> isinstance(Top(Anchovy(), Top(Tuna(), Top(Anchovy(), Bot()))), Pie)
True
>>> a = Top(Anchovy(), Bot()).removeFish(Anchovy())
>>> whatPie(a)
Bot/
"""

from abc import ABC, abstractmethod


class RemoveAnchovy:
    def forBot(self) -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie") -> "Pie":
        if Anchovy().equals(obj):
            return pie.removeAnchovy()
        else:
            return Top(obj, pie.removeAnchovy())


class RemoveFish(object):
    def forBot(self, fish: "Fish") -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie", fish: "Fish") -> "Pie":
        if fish.equals(obj):
            return pie.removeFish(fish)
        else:
            return Top(obj, pie.removeFish(fish))


class Integer(object):
    def __init__(self, value):
        self.value = value

    def equals(self, i: "Integer") -> bool:
        return self.value == i.value


class RemoveInteger(object):
    def forBot(self, i: Integer) -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "pie", i: Integer) -> "Pie":
        if i.equals(obj):
            return pie.removeInteger()
        else:
            return Top(obj, pie.removeInteger(i))


class Pie(ABC):
    removeAnchovyFn = RemoveAnchovy()
    removeFishFn = RemoveFish()

    @abstractmethod
    def removeAnchovy(self) -> "Pie":
        pass

    @abstractmethod
    def removeFish(self) -> "Pie":
        pass


class Bot(Pie):
    def removeAnchovy(self) -> Pie:
        return self.removeAnchovyFn.forBot()

    def removeFish(self, fish: "Fish"):
        return self.removeFishFn.forBot(fish)


class Top(Pie):
    def __init__(self, obj: object, pie: Pie):
        self.obj = obj
        self.pie = pie

    def removeAnchovy(self) -> Pie:
        return self.removeAnchovyFn.forTop(self.obj, self.pie)

    def removeFish(self, fish: "Fish"):
        return self.removeFishFn.forTop(self.obj, self.pie, fish)


class Fish(ABC):
    pass


class Anchovy(Fish):
    def equals(self, obj: object) -> bool:
        return isinstance(obj, Anchovy)


class Salmon(Fish):
    def equals(self, obj: object) -> bool:
        return isinstance(obj, Salmon)


class Tuna(Fish):
    def equals(self, obj: object) -> bool:
        return isinstance(obj, Tuna)


def whatPie(pie: Pie):
    print(pie.__class__.__name__, end="/")
    if hasattr(pie, "pie"):
        whatPie(pie.pie)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

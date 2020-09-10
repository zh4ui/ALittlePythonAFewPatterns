"""
>>> isinstance(Top(Anchovy(), Top(Tuna(), Top(Anchovy(), Bot()))), Pie)
True
>>> a = Top(Anchovy(), Bot()).removeFish(Anchovy())
>>> whatPie(a)
Bot/

>>> b = Top(Integer(2), Top(Integer(3), Top(Integer(2), Bot()))).remove(Integer(3))
>>> whatPie(b)
Top/Top/Bot/

>>> c = Top(Anchovy(), Bot()).remove(Anchovy())
>>> whatPie(c)
Bot/

>>> d = Top(Anchovy(), Top(Integer(3), Top(Zero(), Bot()))).remove(Zero())
>>> whatPie(d)
Top/Top/Bot/
"""

from abc import ABC, abstractmethod

from Num05 import *


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


class RemoveInteger(object):
    def forBot(self, i: "Integer") -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie", i: "Integer") -> "Pie":
        if i.equals(obj):
            return pie.removeInteger(i)
        else:
            return Top(obj, pie.removeInteger(i))


class Remove(object):
    def forBot(self, obj: object) -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie", anything: object) -> "Pie":
        if anything.equals(obj):
            return pie.remove(anything)
        else:
            return Top(obj, pie.remove(anything))


class SubstituteFish(object):
    def forBot(self, new: "Fish", old: "Fish") -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie", new: "Fish", old: "Fish") -> "Pie":
        if obj.equals(old):
            return Top(new, pie.substituteFish(new, old))
        else:
            return Top(old, pie.substituteFish(new, old))


class SubstituteInteger(object):
    def forBot(self, new: "Integer", old: "Integer") -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie", new: "Integer", old: "Integer") -> "Pie":
        if obj.equals(old):
            return Top(new, pie.substitueInteger(new, old))
        else:
            return Top(old, pie.substituteInteger(new, old))


class Substitute(object):
    def forBot(self, new: object, old: object) -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie", new: object, old: object) -> "Pie":
        if obj.equals(old):
            return Top(new, pie.substitute(new, old))
        else:
            return Top(old, pie.substitue(new, old))


class Pie(ABC):
    removeAnchovyFn = RemoveAnchovy()
    removeFishFn = RemoveFish()
    removeFn = Remove()
    substituteFishFn = SubstituteFish()
    substituteIntegerFn = SubstituteInteger()
    substituteFn = Substitute()

    @abstractmethod
    def removeAnchovy(self) -> "Pie":
        pass

    @abstractmethod
    def removeFish(self) -> "Pie":
        pass

    @abstractmethod
    def remove(self, obj: object) -> "Pie":
        pass

    @abstractmethod
    def substituteFish(self, new: "Fish", old: "Fish") -> "Pie":
        pass

    @abstractmethod
    def substitueInteger(self, new: "Integer", old: "Integer") -> "Pie":
        pass

    @abstractmethod
    def substitue(self, new: object, old: object) -> "Pie":
        pass


class Bot(Pie):
    def removeAnchovy(self) -> Pie:
        return self.removeAnchovyFn.forBot()

    def removeFish(self, fish: "Fish"):
        return self.removeFishFn.forBot(fish)

    def remove(self, anything: object) -> Pie:
        return self.removeFn.forBot(anything)

    def substituteFish(self, new: "Fish", old: "Fish"):
        return self.substituteFishFn.forBot(new, old)

    def substitueInteger(self, new: "Integer", old: "Integer") -> "Pie":
        return self.substitueIntegerFn.forBot(new, old)

    def substitue(self, new: object, old: object) -> "Pie":
        return self.substitueFn.forBot(new, old)


class Top(Pie):
    def __init__(self, obj: object, pie: Pie):
        self.obj = obj
        self.pie = pie

    def removeAnchovy(self) -> Pie:
        return self.removeAnchovyFn.forTop(self.obj, self.pie)

    def removeFish(self, fish: "Fish"):
        return self.removeFishFn.forTop(self.obj, self.pie, fish)

    def remove(self, anything: object) -> Pie:
        return self.removeFn.forTop(self.obj, self.pie, anything)

    def substituteFish(self, new: "Fish", old: "Fish"):
        return self.substituteFishFn.forTop(self.obj, self.pie, new, old)

    def substitueInteger(self, new: "Integer", old: "Integer") -> "Pie":
        return self.substitueIntegerFn.forTop(self.obj, self.pie, new, old)

    def substitue(self, new: object, old: object) -> "Pie":
        return self.substituteFn.forTop(self.obj, self.pie, new, old)


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


class Integer(object):
    def __init__(self, value):
        self.value = value

    def equals(self, i: "Integer") -> bool:
        return self.value == i.value


def whatPie(pie: Pie):
    print(pie.__class__.__name__, end="/")
    if hasattr(pie, "pie"):
        whatPie(pie.pie)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

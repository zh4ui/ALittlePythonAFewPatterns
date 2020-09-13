"""
>>> a = Top(Integer(3), Top(Integer(2), Top(Integer(3), Bot())))
>>> a = a.remove(Remove(), Integer(3))
>>> whatPie(a)
Top/Bot/
>>> b = Top(Integer(3), Top(Integer(2), Top(Integer(3), Bot())))
>>> b = b.substitute(Substitute(), Integer(5), Integer(3))
>>> whatPie(b)
Top/Top/Top/Bot/
>>> b.obj.value
5
>>> c = Top(Integer(3), Top(Integer(2), Top(Integer(3), Bot())))
>>> c = c.substitute2(Substitute2(Integer(5), Integer(3)))
>>> whatPie(c)
Top/Top/Top/Bot/
>>> c.obj.value
5
>>> d = Top(Anchovy(), Top(Tuna(), Top(Anchovy(), Top(Tuna(), Top(Anchovy(), Bot())))))
>>> d = d.accept(LimitedSubstitutionVisitor(2,  Salmon(),  Anchovy()))
"""


from abc import ABC, abstractmethod


class Remove(object):
    def forBot(self, par: object) -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie", par: object) -> "Pie":
        if obj.equals(par):
            return pie.remove(self, par)
        else:
            return Top(obj, pie.remove(self, par))


class Substitute(object):
    def forBot(self, new: object, old: object) -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie", new: object, old: object) -> "Pie":
        if obj.equals(old):
            return Top(new, pie.substitute(self, new, old))
        else:
            return Top(obj, pie.substitute(self, new, old))


class Substitute2(object):
    def __init__(self, new: object, old: object):
        self.new = new
        self.old = old

    def forBot(self) -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie") -> "Pie":
        if obj.equals(self.old):
            return Top(self.new, pie.substitute2(self))
        else:
            return Top(self.old, pie.substitute2(self))


class PieVisitor(ABC):
    @abstractmethod
    def forBot(self) -> "Pie":
        pass

    @abstractmethod
    def forTop(self, obj: object, pie: "Pie") -> "Pie":
        pass


class RemoveVisitor(PieVisitor):
    def __init__(self, target: object):
        self.target = target

    def forBot(self) -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie") -> "Pie":
        if obj.equals(self.target):
            return pie.accept(self)
        else:
            return Top(obj, pie.accept(self))


class SubstituteVisitor(PieVisitor):
    def __init__(self, new: object, old: object):
        self.new = new
        self.old = old

    def forBot(self) -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie") -> "Pie":
        if obj.equals(self.old):
            return Top(self.new, pie.accept(self))
        else:
            return Top(obj, pie.accept(self))


class LimitedSubstitutionVisitor(PieVisitor):
    def __init__(self, n: int, new: object, old: object):
        self.n = n
        self.new = new
        self.old = old

    def forBot(self) -> "Pie":
        return Bot()

    def forTop(self, obj: object, pie: "Pie") -> "Pie":
        if self.n == 0:
            return Top(obj, pie)
        elif obj.equals(self.old):
            return Top(self.new, pie.accept(self))
        else:
            return Top(obj, pie.accept(self))


class Pie(ABC):
    @abstractmethod
    def remove(self, fn: Remove, par: object) -> "Pie":
        pass

    @abstractmethod
    def substitute(self, fn: Substitute, new: object, old: object) -> "Pie":
        pass

    @abstractmethod
    def substitute2(self, fn: Substitute2) -> "Pie":
        pass

    @abstractmethod
    def accept(self, visitor: PieVisitor) -> "Pie":
        pass


class Bot(Pie):
    def remove(self, fn: Remove, par: object) -> Pie:
        return fn.forBot(par)

    def substitute(self, fn: Substitute, new: object, old: object) -> Pie:
        return fn.forBot(new, old)

    def substitute2(self, fn: Substitute2) -> Pie:
        return fn.forBot()

    def accept(self, ask: PieVisitor) -> Pie:
        return ask.forBot()


class Top(Pie):
    def __init__(self, obj: object, pie: Pie):
        self.obj = obj
        self.pie = pie

    def remove(self, fn: Remove, par: object) -> Pie:
        return fn.forTop(self.obj, self.pie, par)

    def substitute(self, fn: Substitute, new: object, old: object) -> Pie:
        return fn.forTop(self.obj, self.pie, new, old)

    def substitute2(self, fn: Substitute2) -> Pie:
        return fn.forTop(self.obj, self.pie)

    def accept(self, ask: PieVisitor) -> Pie:
        return ask.forTop(self.obj, self.pie)


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

    def intValue(self):
        return self.value


def whatPie(pie: Pie):
    print(pie.__class__.__name__, end="/")
    if hasattr(pie, "pie"):
        whatPie(pie.pie)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

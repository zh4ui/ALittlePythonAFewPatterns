"""
>>> PiemanM().numTop(Anchovy)
0
"""

from abc import ABC, abstractmethod

from Ch06Pie import Integer, Anchovy


class PieVisitor(ABC):
    @abstractmethod
    def forBot(self, that: "Bot") -> object:
        pass

    @abstractmethod
    def forTop(self, that: "Top") -> object:
        pass


class Pie(ABC):
    @abstractmethod
    def accept(self, ask: PieVisitor) -> object:
        pass


class Bot(Pie):
    def accept(self, ask):
        return ask.forBot(self)


class Top(Pie):
    def __init__(self, t: object, pie: Pie):
        self.t = t
        self.pie = pie

    def accept(self, ask):
        return ask.forTop(self)


class Occurs(PieVisitor):
    def __init__(self, o):
        self.o = o

    def forBot(self, that):
        return Integer(0)

    def forTop(self, that):
        if that.t.equals(self.o):
            return Integer(that.pie.accept(self).intValue() + 1)
        else:
            return that.pie.accept(self)


class Remove(PieVisitor):
    def __init__(self, o: object):
        self.o = o

    def forBot(self, that):
        return Bot()

    def forTop(self, that):
        if self.o.equals(that.t):
            return that.pie.accept(self)
        else:
            return Top(that.t, that.r.accept(self))


class Substitute(PieVisitor):
    def __init__(self, n: object, o: object):
        self.new = n
        self.old = o

    def forBot(self, that):
        return that

    def forTop(self, that):
        if self.old.equals(that.t):
            that.t = n
            that.pie.accept(self)
            return that
        else:
            that.pie.accept(self)
            return that


class PiemanI(ABC):
    @abstractmethod
    def addTop(self, t: object) -> int:
        pass

    @abstractmethod
    def removeTop(self, t: object) -> int:
        pass

    @abstractmethod
    def substitueTop(self, new: object, old: object) -> int:
        pass

    @abstractmethod
    def numTop(self, o: object) -> int:
        pass


class PiemanM(PiemanI):
    def __init__(self):
        self.p = Bot()

    def addTop(self, t):
        self.p = Top(t, self.p)
        return self.occTop(t)

    def removeTop(self, t):
        self.p = self.p.accept(Remove(t))
        return self.occTop(t)

    def substitueTop(self, new, old):
        self.p = self.p.accept(Substitute(n, o))
        return self.occTop(t)

    def numTop(self, o):
        return self.p.accept(Occurs(o)).intValue()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

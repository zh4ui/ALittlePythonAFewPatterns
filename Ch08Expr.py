"""
"""

from abc import ABC, abstractmethod
from typing import Any


class Expr(ABC):
    @abstractmethod
    def accept(self, ask: "ExprVisitor") -> Any:
        pass


class Plus(Expr):
    def __init__(self, lexpr: Expr, rexpr: Expr):
        self.lexpr = lexpr
        self.rexpr = rexpr

    def accept(self, ask):
        ask.forPlus(self.lexpr, self.rexpr)


class Diff(Expr):
    def __init__(self, lexpr: Expr, rexpr: Expr):
        self.lexpr = lexpr
        self.rexpr = rexpr

    def accept(self, ask):
        ask.forDiff(self.lexpr, self.rexpr)


class Prod(Expr):
    def __init__(self, lexpr: Expr, rexpr: Expr):
        self.lexpr = lexpr
        self.rexpr = rexpr

    def accept(self, ask):
        ask.forProd(self.lexpr, self.rexpr)


class Const(Expr):
    def __init__(self, value: object):
        self.value = value

    def accept(self, ask):
        ask.forConst(self.value)


class ExprVisitor(object):
    @abstractmethod
    def forPlus(self, lexpr: Expr, rexpr: Expr) -> Any:
        pass

    @abstractmethod
    def forDiff(self, lexpr: Expr, rexpr: Expr) -> Any:
        pass

    @abstractmethod
    def forProd(self, lexpr: Expr, rexpr: Expr) -> Any:
        pass

    @abstractmethod
    def forConst(self, value: object) -> Any:
        pass


class Integer(object):
    def __init__(self, value: int):
        self.value = value

    def initValue(self) -> int:
        return self.value

    def equals(self, i: "Integer") -> bool:
        return self.value == i.value


class Set(ABC):
    def add(self, i: Integer) -> "Set":
        if self.contain(i):
            return self
        else:
            return Add(i, self)

    @abstractmethod
    def contain(self, i: Integer) -> bool:
        pass

    @abstractmethod
    def plus(self, s: "Set") -> "Set":
        pass

    @abstractmethod
    def diff(self, s: "Set") -> "Set":
        pass

    @abstractmethod
    def prod(self, s: "Set") -> "Set":
        pass


class Empty(Set):
    def contain(self, i: Integer):
        return False

    def plus(self, s):
        return s

    def diff(self, s):
        return Empty()

    def prod(self, s):
        return Empty()


class Add(Set):
    def __init__(self, i: Integer, s: Set):
        self.i = i
        self.s = s

    def contain(self, i: Integer):
        if i.equals(self.i):
            return True
        else:
            return self.s.contain(i)

    def plus(self, t: Set):
        return self.s.plus(t.add(self.i))

    def diff(self, t: Set):
        if t.contain(self.i):
            return self.s.diff(t)
        else:
            return self.s.diff(t).add(self.i)

    def prod(self, t: Set):
        if t.contain(self.i):
            return self.s.prod(t).add(self.i)
        else:
            return self.s.prod(t)


class Eval(ExprVisitor):
    @abstractmethod
    def plus(self, lobj, robj) -> object:
        pass

    @abstractmethod
    def diff(self, lobj, robj) -> object:
        pass

    @abstractmethod
    def prod(self, lobj, robj) -> object:
        pass

    def forPlus(self, lexpr: Expr, rexpr: Expr):
        return self.plus(lexpr.accept(self), rexpr.accept(self))

    def forDiff(self, lexpr: Expr, rexpr: Expr):
        return self.diff(lexpr.accept(self), rexpr.accept(self))

    def forProd(self, lexpr: Expr, rexpr: Expr):
        return self.prod(lexpr.accept(self), rexpr.accept(self))

    def forConst(self, value: object):
        return value


class IntEval(Eval):
    def plus(self, lobj, robj):
        return Integer(lobj.intValue() + robj.intValue())

    def diff(self, lobj, robj):
        return Integer(lobj.intValue() - robj.intValue())

    def prod(self, lobj, robj):
        return Integer(lobj.intValue() * robj.intValue())


class SetEval(Eval):
    def plus(self, lobj, robj):
        return lobj.plus(robj)

    def diff(self, lobj, robj):
        return lobj.diff(robj)

    def prod(self, lobj, robj):
        return lobj.prod(robj)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Plus(Const(Integer(7)), Prod(Diff(Const(Integer(4), Const(Integer(3)))), Const(Integer(5))))
    # Plus(Const(Empty().add(Integer(7)).add(Integer(5))), Prod(Diff(Const(Empty().add(Integer(4))), Const(Empty().add(Integer(3)))), Const(Empty().add(Integer(5)))))

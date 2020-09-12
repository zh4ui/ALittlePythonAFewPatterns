"""
>>> Circle(10).accept(HasPt(CartesianPt(10,10)))
False
>>> Square(10).accept(HasPt(CartesianPt(10,10)))
True
>>> Trans(CartesianPt(5,6), Circle(10)).accept(HasPt(CartesianPt(10,10)))
True

>>> a = Trans(CartesianPt(12,2), Union(Square(10), Trans(CartesianPt(4,4), Circle(5))))
"""

from abc import ABC, abstractmethod
from Ch09Point import *


class Shape(ABC):
    @abstractmethod
    def accept(self, ask) -> bool:
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def accept(self, ask):
        return ask.forCircle(self.radius)


class Square(Shape):
    def __init__(self, side: int):
        self.side = side

    def accept(self, ask):
        return ask.forSqaure(self.side)


class Trans(Shape):
    def __init__(self, q: Point, s: Shape):
        self.q = q
        self.s = s

    def accept(self, ask):
        return ask.forTrans(self.q, self.s)


class Union(Shape):
    def __init__(self, s: Shape, t: Shape):
        self.s = s
        self.t = t

    def accept(self, ask):
        return ask.forUnion(self.s, self.t)


class ShapeVisitor(ABC):
    @abstractmethod
    def forCircle(self, radius: int) -> bool:
        pass

    @abstractmethod
    def forSqaure(self, side: int) -> bool:
        pass

    @abstractmethod
    def forTrans(self, q: Point, s: Shape) -> bool:
        pass


class UnionVisitor(ABC):
    @abstractmethod
    def forUnion(self, s: Shape, t: Shape) -> bool:
        pass


class HasPt(ShapeVisitor):
    def __init__(self, p: Point):
        self.p = p

    def forCircle(self, radius: int) -> bool:
        return self.p.distanceToOrigin() <= radius

    def forSqaure(self, side: int) -> bool:
        return self.p.x <= side and self.p.y <= side

    def forTrans(self, q: Point, s: Shape) -> bool:
        return s.accept(HasPt(self.p.minus(q)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

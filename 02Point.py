"""
>>> pt = CartesianPt(3,4)
>>> pt.distanceToOrigin()
5
>>> pt = ManhattanPt(1,2)
>>> pt.distanceToOrigin()
3

>>> ManhattanPt(3,4).closerToOrigin(ManhattanPt(1,5))
False
>>> CartesianPt(12,5).closerToOrigin(CartesianPt(3,4))
False
>>> CartesianPt(3,4).closerToOrigin(ManhattanPt(1,5))
True
"""

from abc import ABC, abstractmethod
from math import sqrt


class Point(ABC):
    @abstractmethod
    def distanceToOrigin(self) -> int:
        pass

    def closerToOrigin(self, p: "Point") -> bool:
        return self.distanceToOrigin() <= p.distanceToOrigin()


class CartesianPt(Point):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceToOrigin(self) -> int:
        return int(sqrt(self.x ** 2 + self.y ** 2))


class ManhattanPt(Point):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceToOrigin(self) -> int:
        return self.x + self.y


if __name__ == "__main__":
    import doctest

    doctest.testmod()

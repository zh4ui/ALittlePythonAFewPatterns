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

>>> ShadowedManhattanPt(2,3,1,0).distanceToOrigin()
6

>>> ShadowedCartesianPt(12,5,3,4).distanceToOrigin()
17
"""

from abc import ABC, abstractmethod
from math import sqrt


class Point(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def distanceToOrigin(self) -> int:
        pass

    def closerToOrigin(self, p: "Point") -> bool:
        return self.distanceToOrigin() <= p.distanceToOrigin()

    def minus(self, p: "Point") -> "Point":
        return CartesianPt(self.x - p.x, self.y - p.y)


class CartesianPt(Point):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceToOrigin(self) -> int:
        return int(sqrt(self.x ** 2 + self.y ** 2))


class ShadowedCartesianPt(CartesianPt):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y)
        self.dx = dx
        self.dy = dy

    def distanceToOrigin(self):
        return CartesianPt(self.x + self.dx, self.y + self.dy).distanceToOrigin()


class ManhattanPt(Point):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceToOrigin(self) -> int:
        return self.x + self.y


class ShadowedManhattanPt(ManhattanPt):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y)
        self.dx = dx
        self.dy = dy

    def distanceToOrigin(self):
        return super().distanceToOrigin() + self.dx + self.dy


if __name__ == "__main__":
    import doctest

    doctest.testmod()

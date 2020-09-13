"""
>>> a = ManhattanPt(1,4)
>>> a.distanceToOrigin()
5
>>> a.moveBy(2,8)
15
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

    def moveBy(self, dx: int, dy: int) -> int:
        self.x = self.x + dx
        self.y = self.y + dy
        return self.distanceToOrigin()


class CartesianPt(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

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
        super().__init__(x, y)

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

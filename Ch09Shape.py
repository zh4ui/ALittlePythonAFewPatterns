from abc import ABC, abstractmethod
from Ch09Point import *


class Shape(ABC):
    @abstractmethod
    def accept(self, ask: "ShapeVisitor") -> bool:
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def accept(self, ask):
        return ask.forCircle(self.radius)


class Sqaure(Shape):
    def __init__(self, size: int):
        self.size = size

    def accept(self, ask):
        return ask.forSqaure(self.size)


class ShapeVisitor(ABC):
    @abstractmethod
    def forCircle(self, radius: int) -> bool:
        pass

    @abstractmethod
    def forSqaure(self, size: int) -> bool:
        pass

    @abstractmethod
    def forTrans(self, q: Point, s: Shape) -> bool:
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()

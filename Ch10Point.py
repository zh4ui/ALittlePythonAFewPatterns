from abc import ABC, abstractmethod


class Point(ABC):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

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


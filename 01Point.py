from abc import ABC


class Point(ABC):
    pass


class CartesianPt(Point):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class ManhattanPt(Point):
    def __init__(self, x, y):
        self.x = x
        self.y = y


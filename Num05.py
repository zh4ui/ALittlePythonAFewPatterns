from abc import ABC


class Num(ABC):
    pass


class OneMoreThan(Num):
    def __init__(self, num):
        self.predecessor = num

    def equals(self, obj: object) -> bool:
        if isinstance(obj, OneMoreThan):
            return self.predecessor.equals(obj)
        else:
            return False


class Zero(Num):
    def equals(self, obj: object) -> bool:
        return isinstance(obj, Zero)

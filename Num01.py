from abc import ABC


class Num(ABC):
    pass


class Zero(Num):
    pass


class OneMoreThan(Num):
    def __init__(self, num):
        self.num = num


if __name__ == "__main__":

    OneMoreThan(OneMoreThan(Zero()))


"""
>>> Bud().accept(bIsFlat())
True
>>> Bud().accept(bIsSplit())
True

>>> Split(Bud(), Bud()).accept(iHeight())
1

>>> a = Split(Split(Flat(Fig(), Bud()), Flat(Fig(), Bud())), Flat(Fig(), Flat(Lemon(), Flat(Apple(), Bud()))))
>>> a = a.accept(tSubst(Apple(), Fig()))
"""

from abc import ABC, abstractmethod
from typing import Union, Any


class Fruit(ABC):
    pass


class Peach(Fruit):
    def equals(self, obj: Fruit) -> bool:
        return isinstance(obj, Peach)


class Apple(Fruit):
    def equals(self, obj: Fruit) -> bool:
        return isinstance(obj, Apple)


class Pear(Fruit):
    def equals(self, obj: Fruit) -> bool:
        return isinstance(obj, Pear)


class Lemon(Fruit):
    def equals(self, obj: Fruit) -> bool:
        return isinstance(obj, Lemon)


class Fig(Fruit):
    def equals(self, obj: Fruit) -> bool:
        return isinstance(obj, Fig)


class Tree(ABC):
    @abstractmethod
    def accept(self, ask) -> Any:
        pass


class Bud(Tree):
    def accept(self, ask) -> Any:
        return ask.forBud()


class Flat(Tree):
    def __init__(self, fruit: Fruit, tree: Tree):
        self.fruit = fruit
        self.tree = tree

    def accept(self, ask) -> Any:
        return ask.forFlat(self.fruit, self.tree)


class Split(Tree):
    def __init__(self, ltree: Tree, rtree: Tree):
        self.ltree = ltree
        self.rtree = rtree

    def accept(self, ask) -> Any:
        return ask.forSplit(self.ltree, self.rtree)


class bTreeVisitor(ABC):
    @abstractmethod
    def forBud(self) -> bool:
        pass

    @abstractmethod
    def forFlat(self, fruit: Fruit, tree: Tree) -> bool:
        pass

    @abstractmethod
    def forSplit(self, ltree: Tree, rtree: Tree) -> bool:
        pass


class bIsFlat(bTreeVisitor):
    def forBud(self) -> bool:
        return True

    def forFlat(self, fruit: Fruit, tree: Tree) -> bool:
        return tree.accept(self)

    def forSplit(self, ltree: Tree, rtree: Tree) -> bool:
        return False


class bIsSplit(bTreeVisitor):
    def forBud(self) -> bool:
        return True

    def forFlat(self, fruit: Fruit, tree: Tree) -> bool:
        return False

    def forSplit(self, ltree: Tree, rtree: Tree) -> bool:
        return ltree.accept(self) and rtree.accept(self)


class bHasFruit(bTreeVisitor):
    def forBud(self) -> bool:
        return False

    def forFlat(self, fruit: Fruit, tree: Tree) -> bool:
        return True

    def forSplit(self, ltree: Tree, rtree: Tree) -> bool:
        return ltree.accept(self) or rtree.accept(self)


class iTreeVisitor(ABC):
    @abstractmethod
    def forBud(self) -> int:
        pass

    @abstractmethod
    def forFlat(self, fruit: Fruit, tree: Tree) -> int:
        pass

    @abstractmethod
    def forSplit(self, ltree: Tree, rtree: Tree) -> int:
        pass


class iHeight(iTreeVisitor):
    def forBud(self) -> int:
        return 0

    def forFlat(self, fruit: Fruit, tree: Tree) -> int:
        return tree.accept(self) + 1

    def forSplit(self, ltree: Tree, rtree: Tree) -> int:
        l = ltree.accept(self)
        r = rtree.accept(self)
        n = l if l >= r else r
        return n + 1


class tTreeVisitor(ABC):
    @abstractmethod
    def forBud(self) -> Tree:
        pass

    @abstractmethod
    def forFlat(self, fruit: Fruit, tree: Tree) -> Tree:
        pass

    @abstractmethod
    def forSplit(self, ltree: Tree, rtree: Tree) -> Tree:
        pass


class tSubst(tTreeVisitor):
    def __init__(self, new: Fruit, old: Fruit):
        self.new = new
        self.old = old

    def forBud(self) -> Tree:
        return Bud()

    def forFlat(self, fruit: Fruit, tree: Tree) -> Tree:
        if fruit.equals(self.old):
            return Flat(self.new, tree.accept(self))
        else:
            return Flat(fruit, tree.accept(self))

    def forSplit(self, ltree: Tree, rtree: Tree) -> Tree:
        return Split(ltree.accept(self), rtree.accept(self))


class iOccurs(iTreeVisitor):
    def __init__(self, fruit: Fruit):
        self.fruit = fruit

    def forBud(self) -> int:
        return 0

    def forFlat(self, fruit: Fruit, tree: Tree) -> int:
        if fruit.equals(self.fruit):
            return tree.accept(self) + 1
        else:
            return tree.accept(self)

    def forSplit(self, ltree: Tree, rtree: Tree) -> int:
        return ltree.accept(self) + rtree.accept(self)


class TreeVisitor(ABC):
    @abstractmethod
    def forBud(self) -> Any:
        pass

    @abstractmethod
    def forFlat(self, fruit: Fruit, tree: Tree) -> Any:
        pass

    @abstractmethod
    def forSplit(self, ltree: Tree, rtree: Tree) -> Any:
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()

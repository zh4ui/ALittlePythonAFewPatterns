from abc import ABC


class Layer(ABC):
    pass


class Base(Layer):
    def __init__(self, obj):
        self.obj = obj


class Slice(Layer):
    def __init__(self, layer: Layer):
        self.layer = layer


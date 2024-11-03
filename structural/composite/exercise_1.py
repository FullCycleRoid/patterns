from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    data: str
    @abstractmethod
    def addComponent(self, c):
        pass
    @abstractmethod
    def operation(self):
        pass


class Composite(Component):
    def __init__(self, data):
        self.data = data
        self.childrens: List['Component'] = []

    def addComponent(self, c: Component):
        if len(self.childrens) < 15:
            self.childrens.append(c)

    def operation(self):
        ch = ''.join([child.operation() for child in self.childrens])
        return f"{self.data}({ch})"


class Leaf(Component):
    def __init__(self, data):
        self.data = data

    def addComponent(self, c: Component):
        pass

    def operation(self):
        return '----------' + self.data + '\n'

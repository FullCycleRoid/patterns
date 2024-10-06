from abc import ABC
from copy import deepcopy


class AbstractGraphic(ABC):
    def __init__(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0):
        self.x1: int = x1
        self.x2: int = x2
        self.y1: int = y1
        self.y2: int = y2

    def clone(self):
        return deepcopy(self)

    def changeLocation(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self):
        return f'{self.__class__.__name__}({self.x1},{self.y1},{self.x2},{self.y2})'


class Ellipse(AbstractGraphic):
    pass


class Line(AbstractGraphic):
    pass


class Rect(AbstractGraphic):
    pass


class GraphEditor:
    def __init__(self, p0: AbstractGraphic, p1: AbstractGraphic):
        self.p0 = p0
        self.p1 = p1
        self.store = []

    def addGraphic(self, ind, x1, y1, x2, y2):
        tmp_obj = None
        if ind == 0:
            tmp_obj = self.p0.clone()
        if ind == 1:
            tmp_obj = self.p1.clone()

        tmp_obj.changeLocation(x1, y1, x2, y2)
        self.store.append(tmp_obj)

    def drawAll(self):
        l = [el.draw() for el in self.store]
        return ' '.join(l)

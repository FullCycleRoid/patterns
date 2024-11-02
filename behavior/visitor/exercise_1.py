from abc import ABC, abstractmethod


class Element(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteElementA(Element):
    data: int

    def __init__(self, data: int):
        self.data = data

    def GetData(self):
        return self.data

    def SetData(self, newData: int):
        self._data = newData

    def accept(self, v: 'Visitor'):
        # v.visitConcreteElementA()
        pass


class ConcreteElementB(Element):
    data: str

    def __init__(self, data: str):
        self.data = data

    def GetData(self):
        return self.data

    def SetData(self, newData: str):
        self._data = newData

    def accept(self, v: 'Visitor'):
        # v.visitConcreteElementB()
        pass


class ConcreteElementC(Element):
    data: float

    def __init__(self, data: float):
        self.data = data

    def GetData(self):
        return self.data

    def SetData(self, newData: float):
        self._data = newData

    def accept(self, v: 'Visitor'):
        v.visitConcreteElementC()


class ObjectStructure:
    def __init__(self, struc: list['Element']):
        self.__struc: list['Element'] = struc

    def accept(self, v):
        for e in self.__struc:
            e.accept(v)


class Visitor:
    @abstractmethod
    def visitConcreteElementA(self, e):
        pass

    @abstractmethod
    def visitConcreteElementB(self, e):
        pass

    @abstractmethod
    def visitConcreteElementC(self, e):
        pass


class ConcreteVisitor1(Visitor):
    def visitConcreteElementA(self, e):
        pass

    def visitConcreteElementB(self, e):
        pass

    def visitConcreteElementC(self, e):
        pass


class ConcreteVisitor2(Visitor):
    def visitConcreteElementA(self, e):
        pass

    def visitConcreteElementB(self, e):
        pass

    def visitConcreteElementC(self, e):
        pass


class ConcreteVisitor3(Visitor):
    def visitConcreteElementA(self, e):
        pass

    def visitConcreteElementB(self, e):
        pass

    def visitConcreteElementC(self, e):
        pass

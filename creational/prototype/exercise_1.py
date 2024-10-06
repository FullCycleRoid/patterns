from abc import ABC, abstractmethod
from copy import deepcopy


class AbstractPrototype(ABC):
    def __init__(self, data: str, id: int):
        self.data = data
        self.id = id

    def changeId(self, id):
        self.id = id

    def clone(self):
        return deepcopy(self)

    @abstractmethod
    def getInfo(self):
        pass


class ConcretePrototype1(AbstractPrototype):
    def getInfo(self):
        return 'CP1' + '=' + self.data + '=' + str(self.id)


class ConcretePrototype2(AbstractPrototype):
    def getInfo(self):
        return 'CP2' + '=' + self.data + '=' + str(self.id)


class Client:
    def __init__(self, p):
        self.__p = p
        self.results = []

    def operation(self, id):
        obj = self.__p.clone()
        obj.changeId(id)
        info = obj.getInfo()
        self.results.append(info)

    def getObjects(self):
        return ' '.join(self.results)

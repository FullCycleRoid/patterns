from abc import abstractmethod


class Builder:
    def __init__(self):
        self._product = ''

    def buildStart(self):
        self._product = ''

    def buildPartA(self):
        pass

    def buildPartB(self):
        pass

    def buildPartC(self):
        pass

    def getResult(self):
        return self._product


class ConcreteBuilder1(Builder):
    def buildPartA(self):
        self._product += "-1-"

    def buildPartB(self):
        self._product += "-2-"

    def buildPartC(self):
        self._product += "-3-"


class ConcreteBuilder2(Builder):
    def buildPartA(self):
        self._product += "=*="

    def buildPartB(self):
        self._product += "=**="

    def buildPartC(self):
        self._product += "=***="


class Director:
    def __init__(self, b: Builder):
        self.__b: Builder = b

    def getResult(self):
        return self.__b.getResult()

    def construct(self, template):
        self.__b.buildStart()
        for i in template:
            match i:
                case 'A':
                    self.__b.buildPartA()
                case 'B':
                    self.__b.buildPartB()
                case 'C':
                    self.__b.buildPartC()
                case _:
                    continue

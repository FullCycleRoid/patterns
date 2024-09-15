class ConcreteBuilder1:
    def __init__(self):
        pass
        # Implement the "constructor"

    def buildStart(self):
        pass
        # Implement the method

    def buildPartA(self):
        pass
        # Implement the method

    def buildPartB(self):
        pass
        # Implement the method

    def buildPartC(self):
        pass
        # Implement the method

    def getResult(self):
        pass
        # Implement the method

# Implement the ConcreteBuilder2 class


class Director:
    def __init__(self, b):
        self.__b = b

    def getResult(self):
        return self.__b.getResult()

    def construct(self, templat):
        pass
        # Implement the method
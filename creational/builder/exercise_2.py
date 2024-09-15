class BuilderPascal:

    def __init__(self):
        pass
        # Implement the "constructor"

    def buildStart(self, c):
        pass
        # Implement the method

    def buildFirstChar(self, c):
        pass
        # Implement the method

    def buildNextChar(self, c):
        pass
        # Implement the method

    def buildDelim(self):
        pass
        # Implement the method

    def getResult(self):
        pass
        # Implement the method

# Implement the BuilderPyhton and BuilderC classes

class Director:
    def __init__(self, b):
        self.__b = b

    def getResult(self):
        return self.__b.getResult()

    def construct(self, templat):
        self.__b.buildStart(templat[0])
        # Complete the implementation of the method
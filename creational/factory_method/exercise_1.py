class ConcreteProduct1:
    def __init__(self, info):
        pass
        # Implement the "constructor"

    def getInfo(self):
        pass
        # Implement the method

    def transform(self):
        pass
        # Implement the method

# Implement the ConcreteProduct2 class


class Creator:
    def anOperation(self, info):
        p = self.factoryMethod(info)
        p.transform()
        p.transform()
        return p.getInfo()


class ConcreteCreator1(Creator):
    def factoryMethod(self, info):
        pass
        # Implement the method

# Implement the ConcreteCreator2 descendant class;
#   the anOperation method should not be
#   overridden in this class
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

# Implement the ConcreteProduct2 descendant class


class ConcreteCreator1:
    def factoryMethod(self, info):
        return ConcreteProduct1(info)

    def anOperation(self, info):
        p = self.factoryMethod(info)
        p.transform()
        p.transform()
        return p.getInfo()



# Implement the ConcreteCreator2 descendant class
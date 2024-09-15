class Colleague:
    def setMediator(self, m):
        self.__m = m

    def notify(self):
        self.__m.notifyFrom(self)

# Implement the ConcreteColleague1
#   and ConcreteColleague2 descendant classes

class ConcreteMediatorA:
    def __init__(self):
        pass
        # Implement the "constructor"

    def getC1(self):
        pass
        # Implement the method

    def getC2(self):
        pass
        # Implement the method

    def notifyFrom(self, coll):
        pass
        # Implement the method

# Implement the ConcreteMediatorB class
class ConcreteAggregateA:
    def __init__(self, data):
        pass
        # Implement the "constructor"

    def createIterator(self):
        pass
        # Implement the method

    def getData(self):
        pass
        # Implement the method

# Implement the ConcreteAggregateB
#   and ConcreteAggregateC classes

class ConcreteIteratorA:
    def __init__(self, aggr):
        pass
        # Implement the "constructor"

    def first(self):
        pass
        # Implement the method

    def next(self):
        pass
        # Implement the method

    def isDone(self):
        pass
        # Implement the method

    def currentItem(self):
        pass
        # Implement the method

# Implement the ConcreteIteratorB
#   and ConcreteIteratorC classes

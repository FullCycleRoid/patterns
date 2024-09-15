class Subject:
    def __init__(self):
        pass
        # Implement the "constructor"

    def attach(self, observ):
        pass
        # Implement the method

    def detach(self, observ):
        pass
        # Implement the method

    def notify(self):
        pass
        # Implement the method

class ConcreteSubject(Subject):
    def __init__(self):
        pass
        # Implement the "constructor"

    def setState(self, st):
        pass
        # Implement the method

    def getState(self):
        pass
        # Implement the method

class ConcreteObserver:
    def __init__(self, subj, detachInfo):
        pass
        # Implement the "constructor"

    def attach(self):
        pass
        # Implement the method

    def detach(self):
        pass
        # Implement the method

    def getLog(self):
        pass
        # Implement the method

    def update(self):
        pass
        # Implement the method
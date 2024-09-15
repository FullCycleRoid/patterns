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

    def notify(self, info):
        pass
        # Implement the method

class ConcreteSubject(Subject):
    def __init__(self):
        pass
        # Implement the "constructor"

    def setState(self, st):
        pass
        # Implement the method

class ConcreteObserver:
    def __init__(self, detachInfo):
        pass
        # Implement the "constructor"

    def attach(self, subj):
        pass
        # Implement the method

    def detach(self, subj):
        pass
        # Implement the method

    def getLog(self):
        pass
        # Implement the method

    def onInfo(self, sender, info):
        pass
        # Implement the method
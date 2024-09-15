class ConcreteHandler1:
    def __init__(self, successor, id, req1, req2):
        pass
        # Implement the "constructor"

    def handleRequest(self, req):
        pass
        # Implement the method

# Implement the ConcreteHandler2 class

class Client:
    def __init__(self, h):
        self.__h = h

    def sendRequest(self, req):
        self.__h.handleRequest(req)
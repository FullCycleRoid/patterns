class RequestA:
    def __init__(self, param):
        pass
        # Implement the "constructor"

    def getParam(self):
        pass
        # Implement the method

    def toStr(self):
        pass
        # Implement the method

# Implement the RequestB class

class Handler:
    def __init__(self, successor):
        self.__successor = successor

    def handleRequest(self, req):
        pass
        # Implement the method

# Implement the HandlerA and HandlerB descendant classes

class Client:
    def __init__(self, h):
        self.__h = h

    def sendRequest(self, req):
        self.__h.handleRequest(req)
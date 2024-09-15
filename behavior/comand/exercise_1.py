# Implement the Client, ReceiverA and ReceiverB classes

class ConcreteCommandA:
    def __init__(self, recv):
        pass
        # Implement the "constructor"

    def execute(self):
        pass
        # Implement the method

# Implement the ConcreteCommandB class


class Invoker:
    def __init__(self, cmd):
        self.__cmd = cmd

    def invoke(self):
        self.__cmd.execute()
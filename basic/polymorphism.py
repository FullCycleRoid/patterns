class StackNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.__top = None

    def push(self,data):
        self.__top = StackNode(data, self.__top)

    # Use the implementation of the Stack class
    # from the OOP0Begin1 task


class StackC(Stack):
    def __init__(self):
        super().__init__()
        self.__cnt = 0

    def push(self,data):
        super().push(data)
        self.__cnt += 1

    # Use the implementation of the StackC class
    # from the OOP0Begin2 task

def stackTest(s):
    pass
    # Use the body of the stackTest function
    # from the OOP0Begin2 task

class TextView:
    # Do not change the implementation of the class
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__width = 1
        self.__height = 1

    def getOrigin(self):
        return [self.__x, self.__y]

    def setOrigin(self, x, y):
        self.__x = x
        self.__y = y

    def getSize(self):
        return [self.__width, self.__height]

    def setSize(self, width, height):
        self.__width = width
        self.__height = height

class RectShape:
    def __init__(self, x1, y1, x2, y2):
        pass
        # Implement the "constructor"

    def getInfo(self):
        pass
        # Implement the method

    def moveBy(self, a, b):
        pass
        # Implement the method

# Implement the TextShape class
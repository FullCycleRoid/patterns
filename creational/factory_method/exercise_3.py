class Lion:
    def __init__(self, name):
        self.__name = name

    def getInfo(self):
        return "Lion " + self.__name

# Implement the Tiger, Leopard, Gorilla,
#   Orangutan and Chimpanzee classes


class AnimalCreator:
    def getZoo(self, inds, names):
        zoo = []
        for i in range(len(inds)):
            zoo.append(self.createAnimal(inds[i], names[i]))
        return zoo


class CatCreator(AnimalCreator):
    def createAnimal(self, ind, name):
        pass
        # Implement the method


# Implement the ApeCreator descendant class
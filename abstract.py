from abc import ABC,abstractmethod #abstract base classes

class Mammal(ABC):

    @abstractmethod
    def makesound(self):
        pass
    def givesbirth(self):
        pass
class Cat(Mammal) :
    def makesound(self):
        print("It meows and reigns, bitch!")
        return super().makesound()
    
cat = Cat()
cat.makesound()
    


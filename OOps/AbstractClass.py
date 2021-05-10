from abc import ABC,abstractmethod

class Polygon(ABC):
    ''' This Class is Abstract'''
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    def noofsides(self):
        print("Number of sides are three")

class Hexagon(Polygon):
    def noofsides(self):
        print("Number of sides are six")

class Pentagon(Polygon):
    def noofsides(self):
        print("Number of sides are five")



T=Triangle()
T.noofsides()

H=Hexagon()
H.noofsides()

P=Pentagon()
P.noofsides()
print(Polygon.__doc__)
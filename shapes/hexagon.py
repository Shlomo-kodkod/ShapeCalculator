from shape import Shape
import math

class Hexagon(Shape):
    def __init__(self, side):
        self.__side = side
    
    def area(self):
        return (3 * (math.sqrt(3 * (self.__side ** 2)))) / 2
    
    def perimeter(self):
        return self.__side * 6
    
    def __str__(self):
        return f"Hexagon of side {self.__side} , Area: {self.area()}, Perimeter: {self.perimeter()}"
    
    def __repr__(self):
        return f"Hexagon({self.__side})"
  
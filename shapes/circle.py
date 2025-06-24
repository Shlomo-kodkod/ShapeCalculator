from shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    
    def area(self):
        return (self.__radius ** 2) * math.pi
    
    def perimeter(self):
        return self.__radius * (math.pi * 2)
    
    def __str__(self):
        return f"Circle of radius {self.__radius} , Area: {self.area()}, Perimeter: {self.perimeter()}"
    
    def __repr__(self):
        return f"Circle({self.__radius})"
  
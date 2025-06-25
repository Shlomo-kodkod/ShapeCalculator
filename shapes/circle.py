from shapes.shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        self.name = "Circle"
        self.__radius = radius
    
    def area(self):
        try:
            return (self.__radius ** 2) * math.pi
        except Exception as e:
            print(e)
            return 0
    
    def perimeter(self):
        try:
            return self.__radius * (math.pi * 2)
        except Exception as e:
            print(e)
            return  0
    
    def __str__(self):
        return f"{self.name} of radius {self.__radius}. \nArea: {self.area()}. \nPerimeter: {self.perimeter()}.\n"
    
    def __repr__(self):
        return f"{self.name}({self.__radius})\n"
  
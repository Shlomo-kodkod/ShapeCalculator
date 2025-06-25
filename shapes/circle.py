from shapes.shape import Shape
import math

class Circle(Shape):
    
    def __init__(self, radius):
        self.name = "Circle"
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    
    def area(self):
        return (self.radius ** 2) * math.pi
        
    def perimeter(self):
        return self.radius * (math.pi * 2)
        
    def __str__(self):
        return f"{self.name} of radius {self.radius}. \nArea: {self.area()}. \nPerimeter: {self.perimeter()}.\n"
    
    def __repr__(self):
        return f"{self.name}({self.radius})\n"
  
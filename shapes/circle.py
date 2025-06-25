from shapes.shape import Shape
import math

class Circle(Shape):
    
    def __init__(self, radius: float):
        self.name = "Circle"
        self.__radius = radius

    @property
    def radius(self) -> float:
        return self.__radius
    
    def area(self) -> float:
        return (self.radius ** 2) * math.pi
        
    def perimeter(self) -> float:
        return self.radius * (math.pi * 2)
        
    def get_size_info(self) -> str:
        return f"radius {self.radius}"

    def __str__(self) -> str:
        return f"{self.name} of {self.get_size_info()}. \nArea: {self.area()}. \nPerimeter: {self.perimeter()}.\n"
    
    def __repr__(self) -> str:
        return f"{self.name}({self.radius})\n"
  
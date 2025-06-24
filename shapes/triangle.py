from shape import Shape
import math

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.__side1 = side_a
        self.__side2 = side_b
        self.__side3 = side_c
    
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.__side1) * (p - self.__side2) * (p - self.__side3))
    
    def perimeter(self):
        return self.__side1 + self.__side2 + self.__side3
    
    def __str__(self):
        return f"Triangle of side {self.__side1} side {self.__side2} and side {self.__side3}, Area: {self.area()}, Perimeter: {self.perimeter()}"
    
    def __repr__(self):
        return f"Triangle({self.__side1}, {self.__side2}, {self.__side3})"



  
from shape import Shape

class Square(Shape):
    def __init__(self, side):
        self.__side = side
    
    def area(self):
        return self.__side ** 2
    
    def perimeter(self):
        return self.__side * 4
    
    def __str__(self):
        return f"Square of side {self.__side} and height , Area: {self.area()}, Perimeter: {self.perimeter()}"
    
    def __repr__(self):
        return f"Square({self.__side})"
  
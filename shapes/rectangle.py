from shape import Shape

class Rectangle(Shape):
    def __init__(self, side, height):
        self.name = "Rectangle"
        self._side = side
        self._height = height
    
    def area(self):
        return self._side * self._height
    
    def perimeter(self):
        return (self._side * 2) + (self._height * 2)
    
    def get_size_info(self):
        return f"side {self._side} and height {self._height}"

    def __str__(self):
        return f"{self.name} of {self.get_size_info()}, Area: {self.area()}, Perimeter: {self.perimeter()}"
    
    def __repr__(self):
        return f"{self.name}({self._side}, {self._height})"

    
  
from shapes.shape import Shape

class Rectangle(Shape):
    def __init__(self, side, height):
        self.name = "Rectangle"
        self.__side = side
        self.__height = height
    
    @property
    def side(self):
        return self.__side
    
    @property
    def height(self):
        return self.__height

    def area(self):
        return self.side * self.height
    
    def perimeter(self):
        return (self.side * 2) + (self.height * 2)
    
    def get_size_info(self):
        return f"side {self.side} and height {self.height}"

    def __str__(self):
        return f"{self.name} of {self.get_size_info()}. \nArea: {self.area()}. \nPerimeter: {self.perimeter()}.\n"
    
    def __repr__(self):
        return f"{self.name}({self._side}, {self._height}).\n"

    
  
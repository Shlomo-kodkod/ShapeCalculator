from shapes.shape import Shape

class Rectangle(Shape):
    
    def __init__(self, side: float, height: float):
        self.name = "Rectangle"
        self.__side = side
        self.__height = height
    
    @property
    def side(self) -> float:
        return self.__side
    
    @property
    def height(self) -> float:
        return self.__height

    def area(self) -> float:
        return self.side * self.height
    
    def perimeter(self) -> float:
        return (self.side * 2) + (self.height * 2)
    
    def get_size_info(self) -> str:
        return f"side {self.side} and height {self.height}"

    def __str__(self) -> str:
        return f"{self.name} of {self.get_size_info()}. \nArea: {self.area()}. \nPerimeter: {self.perimeter()}.\n"
    
    def __repr__(self) -> float:
        return f"{self.name}({self.side}, {self.height}).\n"

    
  
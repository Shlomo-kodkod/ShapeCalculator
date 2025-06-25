from shapes.shape import Shape
import math

class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.name = "Triangle"
        self.__side1 = side_a
        self.__side2 = side_b
        self.__side3 = side_c
    
    @property
    def side1(self) -> float:
        return self.__side1
    
    @property
    def side2(self) -> float:
        return self.__side2
    
    @property
    def side3(self) -> float:
        return self.__side3

    def area(self) -> float:
        p = self.perimeter() / 2
        area_s = p * (p - self.side1) * (p - self.side2) * (p - self.side3)
        if area_s < 0:
            print("Invalid triangle dimensions")
            return 0
        return math.sqrt(area_s)

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

    def get_size_info(self) -> str:
        return f"side {self.side1} side {self.side2} and {self.side3}"

    def __str__(self) -> str:
        return f"{self.name} of {self.get_size_info()}. \nArea: {self.area()}. \nPerimeter: {self.perimeter()}.\n"
    
    def __repr__(self) -> str:
        return f"{self.name}({self.side1}, {self.side2}, {self.side3})\n"




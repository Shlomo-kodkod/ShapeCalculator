from shapes.shape import Shape
import math

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.name = "Triangle"
        self._side1 = side_a
        self._side2 = side_b
        self._side3 = side_c
    
    def area(self):
        try:
            p = self.perimeter() / 2
            return math.sqrt(p * (p - self._side1) * (p - self._side2) * (p - self._side3))
        except Exception as e:
            print(e)
            return 0

    def perimeter(self):
        return self._side1 + self._side2 + self._side3

    def get_size_info(self):
        return f"side {self._side1} side {self._side2} and {self._side3}"

    def __str__(self):
        return f"{self.name} of {self.get_size_info()}. \nArea: {self.area()}. \nPerimeter: {self.perimeter()}.\n"
    
    def __repr__(self):
        return f"{self.name}({self._side1}, {self._side2}, {self._side3})\n"




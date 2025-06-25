from shapes.rectangle import Rectangle
import math

class RightTriangle(Rectangle):
    
    def __init__(self, cathetus1: float, cathetus2: float):
        super().__init__(cathetus1, cathetus2)
        self.name = "RightTriangle"

    def area(self) -> float:
        return super().area() / 2
    
    def perimeter(self) -> float:
        hypotenuse = math.sqrt((self.height ** 2) + (self.side ** 2))
        return hypotenuse + self.side + self.height
        

        



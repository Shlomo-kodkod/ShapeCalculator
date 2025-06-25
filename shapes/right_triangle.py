from .rectangle import Rectangle
import math

class RightTriangle(Rectangle):
    def __init__(self, cathetus1, cathetus2):
        super().__init__(cathetus1, cathetus2)
        self.name = "RightTriangle"

    def area(self):
        return super().area() / 2
    
    def perimeter(self):
        hypotenuse = math.sqrt((self.height ** 2) + (self.side ** 2))
        return hypotenuse + self.side + self.height
        

        



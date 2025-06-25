from shapes.square import Square
import math

class Hexagon(Square):
    def __init__(self, side):
        super().__init__(side)
        self.name = "Hexagon"
    
    def area(self):
        return (3 * math.sqrt(3) * (self.side ** 2)) / 2


    def perimeter(self):
        return self.side * 6
    
    def get_size_info(self):
        return f"side {self.side}"
    
    def __repr__(self):
        return f"{self.name}({self.side}).\n"
  


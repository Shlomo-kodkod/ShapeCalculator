from shapes.square import Square
import math

class Hexagon(Square):
    def __init__(self, side):
        super().__init__(side)
        self.name = "Hexagon"
    
    def area(self):
        try:
            return (3 * (math.sqrt(3 * (self._side ** 2)))) / 2
        except Exception as e:
            print(e)
            return  0

    def perimeter(self):
        return self._side * 6
    
    def get_size_info(self):
        return f"side {self._side}"
    
    def __repr__(self):
        return f"{self.name}({self._side}).\n"
  


from shape import Shape

class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        self.__shape = "Rectangle"
        self.__side1 = side_a
        self.__side2 = side_b
    
    def area(self):
        return self.__side1 * self.__side2
    
    def perimeter(self):
        return (self.__side1 * 2) + (self.__side2 * 2)
    
    def __str__(self):
        return f"Shape: {self.__shape}, \nArea: {self.area()}, \nPerimeter: {self.perimeter()}"
    

    


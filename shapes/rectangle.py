from shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    def area(self):
        return self.__width * self.__height
    
    def perimeter(self):
        return (self.__width * 2) + (self.__height * 2)
    
    def __str__(self):
        return f"Rectangle of width {self.__width} and height {self.__height}, Area: {self.area()}, Perimeter: {self.perimeter()}"
    
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    
  
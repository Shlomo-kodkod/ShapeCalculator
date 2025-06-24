from shapes.shape import Shape
from shapes.circle import Circle
from shapes.hexagon import Hexagon
from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle

def is_valid_num(number):
    try:
        number = float(number)
        return True
    except Exception as e:
        print("Invalid value. Please try again.")
        return False

def create_circle():
    radius = input("Enter the radius:")
    while not is_valid_num(radius):
        radius = input("Enter the radius:")
    return Circle(float(radius))

def create_hexagon():
    side = input("Enter the side:")
    while not is_valid_num(side):
        side = input("Enter the side:")
    return Hexagon(float(side))

def create_rectangle():
    width = input("Enter the width:")
    height = input("enter the height:")
    while not is_valid_num(width) or not is_valid_num(height):
        width = input("Enter the width:")
        height = input("enter the height:")
    return Rectangle(float(width), float(height))

def create_square():
    side = input("Enter the side:")
    while not is_valid_num(side):
        side = input("Enter the side:")
    return Square(float(side))

def create_triangle():
    side1 = input("Enter the first side:")
    side2 = input("Enter the second side:")
    side3 = input("Enter the third side:")
    while not all(is_valid_num(i) for i in (side1, side2, side3)):
        side1 = input("Enter the first side:")
        side2 = input("Enter the second side:")
        side3 = input("Enter the third side:")
    return Triangle(float(side1), float(side2), float(side3))

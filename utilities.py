from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.hexagon import Hexagon
from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.right_triangle import RightTriangle


def is_positive(number):
    print("This number can't be negative.") if float(number) < 0 else None
    return float(number) >= 0

def is_valid_num(number):
    try:
        float(number)
        return is_positive(number)
    except Exception:
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
    sides = [input("Enter side {num}: ".format(num = i)) for i in range(1,4)]
    while not all(is_valid_num(i) for i in (sides[0], sides[1], sides[2])):
        sides = [input("Enter side {num}: ".format(num=i)) for i in range(1, 4)]
    return Triangle(float(sides[0]), float(sides[1]), float(sides[2]))

def create_right_triangle():
    cathetus = [input("Enter cathetus {num}: ".format(num=i)) for i in range(1, 3)]
    while not all(is_valid_num(i) for i in (cathetus[0], cathetus[1])):
        cathetus = [input("Enter cathetus {num}: ".format(num=i)) for i in range(1, 3)]
    return RightTriangle(float(cathetus[0]), float(cathetus[1]))


from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.hexagon import Hexagon
from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.right_triangle import RightTriangle


def is_positive(number: str) -> bool:
    print("This number can't be negative.") if float(number) < 0 else None
    return float(number) >= 0

def is_valid_num(number: str) -> bool:
    try:
        float(number)
        return is_positive(number)
    except ValueError:
        print("Invalid value. Please try again.")
        return False

def get_valid_num(input_txt: str) -> float:
    res = input(input_txt)
    while not is_valid_num(res):
        res = input(input_txt)
    return float(res)

def create_circle() -> Circle:
    radius = get_valid_num("Enter the radius:")
    return Circle(radius)

def create_hexagon() -> Hexagon:
    side = get_valid_num("Enter the side:")
    return Hexagon(side)

def create_rectangle() -> Rectangle:
    width = get_valid_num("Enter the width:")
    height = get_valid_num("enter the height:")
    return Rectangle(width, height)

def create_square() -> Square:
    side = get_valid_num("Enter the side:")
    return Square(side)

def create_triangle() -> Triangle:
    sides = [get_valid_num("Enter side {num}: ".format(num = i)) for i in range(1,4)]
    return Triangle(sides[0], sides[1], sides[2])

def create_right_triangle() -> RightTriangle:
    cathetus = [get_valid_num("Enter cathetus {num}: ".format(num=i)) for i in range(1, 3)]
    return RightTriangle(cathetus[0], cathetus[1])


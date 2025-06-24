from shapes.shape import Shape
from shapes.circle import Circle
from shapes.hexagon import Hexagon
from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle
from calculator import is_valid_choice

def creat_circle():
    radius = input("Enter the radius:")
    while not is_valid_choice(radius, 4):
        radius = input("Enter the radius:")
    return Circle(float(radius))

def creat_hexagon():
    side = input("Enter the side:")
    while not is_valid_choice(side, 5):
        radius = input("Enter the side:")
    return Hexagon(float(side))


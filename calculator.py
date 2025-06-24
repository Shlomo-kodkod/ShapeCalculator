from shapes.circle import Circle
from shapes.hexagon import Hexagon
from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle

SHAPES_OPTIONS  = (1,2,3,4,5,0)
CALC_OPTION = (1,2,0)

def display_menu():
    print("-" * 30 + "\n" +
    "Shape Calculator Menu".center(30) + "\n" +
    "-" * 30 + "\n" +
    "Chose shape to calculate\n" + 
    "1.Rectangle\n" +
    "2.Square\n" +
    "3.Triangle\n" +
    "4.Circle\n" +
    "5.Hexagon\n" + 
    "0.Exit\n")

def display_calc_option():
    print("Enter your choice:\n" +
          "1.Get shape area\n" +
          "2.Get shape perimeter\n" +
          "0. Exit\n")

def is_valid_choice(choice, options):
    try:
        res = float(choice)
        return res in options
    except Exception as e:
        print("Invalid choice. Please try again.")
        return False

def get_choice(options):
    choice = input("Enter your choice:\n")
    while not is_valid_choice(choice, options):
        choice = input("Enter your choice:\n")
    return float(choice)

def creat_circle():
    radius = input("Enter the radius:")
    while not is_valid_choice(radius, 1):
        radius = input("Enter the radius:")
    return Circle(float(radius))

def creat_shape(choice):
    pass

def display_calculate(choice: int):
    pass



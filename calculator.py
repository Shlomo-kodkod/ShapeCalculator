from shapes.shape import Shape
import utilities as ut
import time

class Calculator:
        
    SHAPES_OPTIONS  = (1,2,3,4,5,6,0)
    MENU = """ 
       ********** 
  Shape Calculator Menu   
       ********** 
==========================
 Chose shape to calculate:
 [1] Rectangle
 [2] Square
 [3] Triangle
 [4] Circle
 [5] Hexagon
 [6] Right Triangle
 [0] Exit
==========================
    """

    @staticmethod
    def display_menu() -> None:
        print(Calculator.MENU)

    @staticmethod
    def is_valid_choice(choice: str) -> bool:
        try:
            res = int(choice)
            print("Invalid choice. Please try again.")if res not in Calculator.SHAPES_OPTIONS else None
            return res in Calculator.SHAPES_OPTIONS
        except ValueError:
            print("Invalid choice. Please try again.")
            return False

    @staticmethod
    def get_choice() -> int:
        choice = input("Enter your choice:\n")
        while not Calculator.is_valid_choice(choice):
            choice = input("Enter your choice:\n")
        return int(choice)

    @staticmethod
    def create_shape(choice: int) -> Shape:
        shape_map = {
        1: ut.create_rectangle, 2: ut.create_square,
        3: ut.create_triangle, 4: ut.create_circle,
        5: ut.create_hexagon, 6: ut.create_right_triangle}
        return shape_map[choice]()

    @staticmethod
    def calculate() -> None:
        choice = -1
        while choice != 0:
            print("Loading...")
            time.sleep(0.7)
            Calculator.display_menu()
            choice = Calculator.get_choice()
            if choice == 0:
                print("Exit...")
                break
            shape = Calculator.create_shape(choice)
            print(shape)







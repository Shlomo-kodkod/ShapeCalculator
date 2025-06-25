import utilities as ut
import time

class Calculator:
        
    SHAPES_OPTIONS  = (1,2,3,4,5,6,0)

    @staticmethod
    def display_menu():
        print("-" * 30 + "\n" +
        "Shape Calculator Menu".center(30) + "\n" +
        "-" * 30 + "\n" +
        "Chose shape to calculate\n" + 
        "1.Rectangle\n" + "2.Square\n" +
        "3.Triangle\n" + "4.Circle\n" +
        "5.Hexagon\n" + "6.Right Triangle\n"
        "0.Exit\n")

    @staticmethod
    def is_valid_choice(choice):
        try:
            res = int(choice)
            print("Invalid choice. Please try again.")if res not in Calculator.SHAPES_OPTIONS else None
            return res in Calculator.SHAPES_OPTIONS
        except ValueError:
            print("Invalid choice. Please try again.")
            return False

    @staticmethod
    def get_choice():
        choice = input("Enter your choice:\n")
        while not Calculator.is_valid_choice(choice):
            choice = input("Enter your choice:\n")
        return int(choice)

    @staticmethod
    def create_shape(choice):
        shape_map = {
        1: ut.create_rectangle, 2: ut.create_square,
        3: ut.create_triangle, 4: ut.create_circle,
        5: ut.create_hexagon, 6: ut.create_right_triangle}
        return shape_map[choice]()

    @staticmethod
    def calculate():
        choice = -1
        while choice != 0:
            print("Loading...")
            time.sleep(1)
            Calculator.display_menu()
            choice = Calculator.get_choice()
            if choice == 0:
                print("Exit...")
                break
            shape = Calculator.create_shape(choice)
            print(shape)







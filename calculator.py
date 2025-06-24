import utilities as ut

class Calculator:
        
    SHAPES_OPTIONS  = (1,2,3,4,5,0)
    CALC_OPTION = (1,2,0)

    @staticmethod
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

    staticmethod
    def display_calc_option():
        print("\n1.Get shape area\n" +
            "2.Get shape perimeter\n")

    @staticmethod
    def is_valid_choice(choice, options):
        try:
            res = int(choice)
            print("Invalid choice. Please try again.")if res not in options else None
            return res in options
        except Exception as e:
            print("Invalid choice. Please try again.")
            return False

    @staticmethod
    def get_choice(options):
        choice = input("Enter your choice:\n")
        while not Calculator.is_valid_choice(choice, options):
            choice = input("Enter your choice:\n")
        return int(choice)

    @staticmethod
    def create_shape(choice):
        shape_map = {
        1: ut.create_rectangle, 2: ut.create_square,
        3: ut.create_triangle, 4: ut.create_circle,
        5: ut.create_hexagon }
        return shape_map[choice]()

    @staticmethod
    def get_calc(shape):
        Calculator.display_calc_option()
        calc = Calculator.get_choice((1, 2))
        if calc == 1:
            return f"The area is: {shape.area()}\n"
        elif calc == 2:
            return f"The perimeter is: {shape.perimeter()}\n"
        return ""

    @staticmethod
    def calculate():
        choice = -1
        while choice != 0:
            Calculator.display_menu()
            choice = Calculator.get_choice((1, 2, 3, 4, 5, 0))
            if choice == 0:
                print("Exit...")
                break
            shape = Calculator.create_shape(choice)
            print(Calculator.get_calc(shape))







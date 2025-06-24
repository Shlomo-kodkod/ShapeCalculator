import utilities as ut

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
    print("\n1.Get shape area\n" +
          "2.Get shape perimeter\n")

def is_valid_choice(choice, options):
    try:
        res = int(choice)
        print("Invalid choice. Please try again.")if res not in options else None
        return res in options
    except Exception as e:
        print("Invalid choice. Please try again.")
        return False

def get_choice(options):
    choice = input("Enter your choice:\n")
    while not is_valid_choice(choice, options):
        choice = input("Enter your choice:\n")
    return int(choice)

def create_shape(choice):
    shape_map = {
    1: ut.create_rectangle, 2: ut.create_square,
    3: ut.create_triangle, 4: ut.create_circle,
    5: ut.create_hexagon }
    return shape_map[choice]()

def get_calc(shape):
    display_calc_option()
    calc = get_choice((1, 2))
    if calc == 1:
        return shape.area()
    elif calc == 2:
        return shape.perimeter()
    return 0

def calculate():
    choice = -1
    while choice != 0:
        display_menu()
        choice = get_choice((1, 2, 3, 4, 5, 0))
        if choice == 0:
            break
        shape = create_shape(choice)
        print(get_calc(shape))







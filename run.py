# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from colorama import init, Fore
init(autoreset=True)


GAME_SIZE = 5
NAME = ""
PLAYER_FLEET = []
ENEMY_FLEET = []

def display_title():
    """
    This function diplays the ASCII art ship
    """
    print('               |    |    |    ')             
    print('              )_)  )_)  )_)   ')           
    print('             )___))___))___)  ')          
    print('            )____)____)_____) ')
    print('          _____|____|____|______')
    print(Fore.BLUE + ' ---------', Fore.WHITE + '\                    /', Fore.BLUE + '---------')
    print(Fore.BLUE + '         ^^^^^ ^^^^^^^^^^^^^^^^^^^^^')
    print(Fore.BLUE + '        ^^^^      ^^^^     ^^^    ^^')
    print(Fore.BLUE + '                 ^^^^      ^^^')
    print('Welcome to Battleships! a nautical game of tactics.\n')


def collect_name():
    global NAME
    NAME = input("Please input your name:\n")

def clear(num):
    for i in range(num): print("") 

# def create_grid(game_size):
#     """
#     This function creates a list, containing 5 lists, each containing a string "~" to display the grid cordinates.
#     """
#     grid_array = []
#     column = []
#     for x in range(game_size):
#         column.append("~")
#     for y in range(game_size):
#         grid_array.append(column)
#     return grid_array


def display_grid(name, player_grid, enemy_grid):
    """
    This function displays the two battlegrids for the player and the enemy.
    """
    print(f"")
    # 1st row
    frow = (f"  ")
    for x in range(GAME_SIZE):
        frow = frow + f"| {x+1} "
    frow = frow + "|"
    print((GAME_SIZE*1)*" " + "Your Fleet" + (GAME_SIZE*3+2)*" " + frow)
    print((GAME_SIZE*4+4)*"-" + "   ||   " + (GAME_SIZE*4+4)*"-")

    # rows 2+
    for y in range(GAME_SIZE):
        row = f"  "  
        grid_list = player_grid[y]
        for x in range(GAME_SIZE):
            row = row + f"| {grid_list[x]} "
        row = row + f"|    ||   {y+1} "
        grid_list = enemy_grid[y]
        for x in range(GAME_SIZE):
            row = row + f"| {grid_list[x]} "
        row = row + "|"
        print(row)
        print((GAME_SIZE*4+4)*"-" + "   ||   " + (GAME_SIZE*4+4)*"-")

def random_coordinates():
    coordinates = {"x" : 0, "y" : 0}
    coordinates["x"] = random.randrange(0,5)
    coordinates["y"] = random.randrange(0,5)
    return coordinates

def random_coordinates_x_gamesize(fleet):
    cord_set = []
    while len(cord_set) < GAME_SIZE:
        cord = random_coordinates()
        if coordinate_validation(cord, cord_set):
            continue
        else:
            cord_set.append(cord)
    if fleet == 1:
        global PLAYER_FLEET
        PLAYER_FLEET = cord_set
    print(cord_set)
    
def coordinate_validation(cord, cord_set):
    for existing_cord in cord_set:
        if cord["x"] == existing_cord["x"] and cord["y"] == existing_cord["y"]:
            return True

def replace_grid_cords(cords, grid, char):
    """
    This Function takes the cordinates received in a dict format with X and Y values and updates the list item in the grid with the char(acter)
    """
    x = cords["x"]
    y = cords["y"]
    y_grid = grid[y]
    y_grid[x] = char

def show_player_fleet_on_grid(grid, fleet):
    """
    
    """

if __name__ == "__main__":
    display_title()
    collect_name()
    print(NAME)
    random_coordinates_x_gamesize(1)
    random_coordinates_x_gamesize(ENEMY_FLEET)
    print(PLAYER_FLEET)




print(f"Welcome to the battle Captain {NAME}, Your fleet awaits\n")

player_grid = [['~', '~', '~', '~', '~'], ['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~']]
enemy_grid = [['~', '~', '~', '~', '~'], ['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~']]





# PLAYER_FLEET = random_coordinates_x_gamesize()
# display_grid(NAME, player_grid, enemy_grid)


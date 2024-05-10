# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


def display_title():
    """
    This function diplays the ASCII art ship
    """
    print('               |    |    |    ')             
    print('              )_)  )_)  )_)   ')           
    print('             )___))___))___)  ')          
    print('            )____)____)_____) ')
    print('          _____|____|____|______')
    print(' ---------\\                   /---------')
    print('         ^^^^^ ^^^^^^^^^^^^^^^^^^^^^')
    print('        ^^^^      ^^^^     ^^^    ^^')
    print('                 ^^^^      ^^^')
    print('Welcome to Battleships! a nautical game of tactics.\n')


def collect_name():
    name = input("Please input your name:\n")
    return name

def clear(num):
    for i in range(num): print("") 

def create_grid(game_size):
    """
    This function creates a list, containing 5 lists, each containing a string "~" to display the grid cordinates.
    """
    grid_array = []
    column = []
    for x in range(game_size):
        column.append("~")
    for y in range(game_size):
        grid_array.append(column)
    return grid_array


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

def random_coordinates_x_gamesize():
    cord_set = []
    while len(cord_set) < GAME_SIZE:
        cord = random_coordinates()
        if coordinate_validation(cord, cord_set):
            continue
        else:
            cord_set.append(cord)
    print(cord_set)
    return cord_set
    
def coordinate_validation(cord, cord_set):
    for existing_cord in cord_set:
        if cord["x"] == existing_cord["x"] and cord["y"] == existing_cord["y"]:
            return True

display_title()
NAME = collect_name()
print(f"Welcome to the battle Captain {NAME}, Your fleet awaits\n")
GAME_SIZE = 5
player_grid = create_grid(GAME_SIZE)
enemy_grid = create_grid(GAME_SIZE)
display_grid(NAME, player_grid, enemy_grid)
PLAYER_FLEET = random_coordinates_x_gamesize()
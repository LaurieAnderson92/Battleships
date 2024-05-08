# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


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

def create_cordinates(game_size):
    grid_array = []
    column = []
    for x in range(game_size):
        column.append("~")
    for y in range(game_size):
        grid_array.append(column)
    return grid_array

def display_grid(name, grid):
    """
    This funtion displays a battle grid for the player
    """
    # first row
    frow = (f"  ")
    for x in range(GAME_SIZE):
        frow = frow + f"| {x+1} "
    frow = frow + "| "
    print(frow)
    print((GAME_SIZE*4+4)*"-")

    # rows 2-6
    grid_list = 0
    grid[2][4] = "X"
    for y in range(GAME_SIZE):
        row = f"{y+1} "  
        list_index = 0
        for x in range(GAME_SIZE):
            row = row + f"| {grid[grid_list][list_index]} "
            list_index + 1
        row = row + "| "
        print(row)
        grid_list + 1
        print((GAME_SIZE*4+4)*"-")

display_title()
NAME = collect_name()
clear(80)
print(f"Welcome to the battle Captain {NAME}, Your fleet awaits")
GAME_SIZE = 5
player_grid = create_cordinates(GAME_SIZE)
enemy_grid = create_cordinates(GAME_SIZE)
display_grid(NAME, player_grid)
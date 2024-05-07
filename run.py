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
    print(grid_array)

display_title()
NAME = collect_name()
clear(80)
print(f"Welcome to the battle Captain {NAME}, Your fleet awaits")
GAME_SIZE = 5
create_cordinates(GAME_SIZE)
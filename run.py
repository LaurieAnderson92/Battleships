# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from colorama import init, Fore
init(autoreset=True)


GAME_SIZE = 5
NAME = ""
player_fleet = []
enemy_fleet = []
player_grid = [['~', '~', '~', '~', '~'], ['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~']]
enemy_grid = [['~', '~', '~', '~', '~'], ['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~']]
coordinates = {}
player_shots = []
enemy_shots = []


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
    print(f"Welcome to the battle Captain {NAME}, Your fleet awaits\n")

def clear(num):
    for i in range(num): print("") 

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
        global player_fleet
        player_fleet = cord_set
    elif fleet == 2:
        global enemy_fleet
        enemy_fleet = cord_set
    
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
    This funtions takes the cordinates of the PLAYER_FLEET and changes the display on the grid
    """
    global player_grid
    for cords in fleet:
        replace_grid_cords(cords, player_grid, Fore.GREEN+"@"+Fore.WHITE)

def enter_coordinates():
    """
    This functions receives a set of coordinates via two inputs and returns a dict of cordinates
    """
    coordinates = {"x" : 0, "y" : 0}
    while True:
        try:
            coordinates["x"] = int(input("Place your shot along the X axsis: \n")) - 1
            coordinates["y"] = int(input("Place your shot along the Y axsis: \n")) - 1
            if (coordinates["x"] < 0 or coordinates["x"] > 4) or (coordinates["y"] < 0 or coordinates["y"] > 4):
                print(f"Captain, these cordinates are invalid! Please enter cordinates between 1 and 5")
            else:
                break
        except ValueError:
            print("Captain,that's not even a number! Please enter cordinates between 1 and 5")
    return coordinates

def turn_retrieve_cordinates(shooter):
    """
    This function generates the battle cordinates based on the shooter input, 0 for player, 1 for enemy
    """
    global coordinates
    if shooter == 0:
        coordinates = enter_coordinates()
    elif shooter == 1:
        coordinates = random_coordinates()

def turn_check_for_hit(coordinates, fleet, grid, player):
    """
    This function takes the global cordinates and cycles through the list of ships in the fleet, judging weither it's a hit or a miss.
    """
    hit_found = False
    for ship in fleet:
        if (coordinates["x"] == ship["x"]) and (coordinates["y"] == ship["y"]):
            fleet.remove(ship)
            if player == 0:
                print(f"Success Captain {NAME}! You have hit one of the enemy's ships.")
                global enemy_fleet
                global player_shots
                enemy_fleet = fleet
                player_shots.append(coordinates)
            else:
                print(f"Avast Captain {NAME}! They have hit one of our ships.")
                global player_fleet
                global enemy_shots
                player_fleet = fleet
                enemy_shots.append(coordinates)
            hit_found = True
            replace_grid_cords(coordinates, grid, Fore.RED+"X"+Fore.WHITE)
            break
    if not hit_found:
        if player == 0:
            print(f"Miss Captain {NAME}, Your shot missed the enemy's fleet.")
        else:
            print(f"What fortune Captain {NAME}! their shot missed our fleet.")
        replace_grid_cords(coordinates, grid, "X")


if __name__ == "__main__":
    display_title()
    collect_name()
    random_coordinates_x_gamesize(1)
    random_coordinates_x_gamesize(2)
    show_player_fleet_on_grid(player_grid, player_fleet)
    display_grid(NAME, player_grid, enemy_grid)
    #Start the gameplay loop
    while (len(player_fleet)) > 0 and (len(enemy_fleet) > 0):
        turn_retrieve_cordinates(0)
        clear(5)
        turn_check_for_hit(coordinates, enemy_fleet, enemy_grid, 0)
        print("The enemy is returning fire!")
        turn_retrieve_cordinates(1)
        turn_check_for_hit(coordinates, player_fleet, player_grid, 1)
        display_grid(NAME, player_grid, enemy_grid)
        print(f"Player shots {player_shots}")
        if len(player_fleet) == 0:
            print("The game has ended in defeat.")
        elif len(enemy_fleet) == 0:
            print("The game has ended in victory!")

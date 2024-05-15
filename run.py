"""This file runs a game of battleships in the terminal."""
# Imports and requirements
import random
import os
from colorama import init, Fore
# Below function from colorama auto resets the color to white for every line.
init(autoreset=True)

# Global variables
GAME_SIZE = 5
NAME = ""
player_fleet = []
enemy_fleet = []
player_grid = [
    ['~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~']
    ]
enemy_grid = [
    ['~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~']
    ]
coordinates = {}
player_shots = []
enemy_shots = []


def display_title():
    """Create a ASCII art ship."""
    print('               |    |    |    ')
    print('              )_)  )_)  )_)   ')
    print('             )___))___))___)  ')
    print('            )____)____)_____) ')
    print('          _____|____|____|______')
    print(
        Fore.BLUE + ' --------',
        Fore.WHITE + '|                   /',
        Fore.BLUE + '---------'
    )
    print(Fore.BLUE + '         ^^^^^ ^^^^^^^^^^^^^^^^^^^^^')
    print(Fore.BLUE + '        ^^^^      ^^^^     ^^^    ^^')
    print(Fore.BLUE + '                 ^^^^      ^^^')
    print('Welcome to Battleships! a nautical game of tactics.\n')


def collect_name():
    """
    Collect the input from the player.

    It is later used as a variable.
    """
    global NAME
    while True:
        NAME = input("Please input your name:\n")
        if NAME.isalpha() and len(NAME) <= 12:
            break
        else:
            print("Captain, that name need to change. " + 
            "Please it to under 12 characters using only a-z"
                  )
    print(f"Welcome to the battle Captain {NAME}, Your fleet awaits\n")


# This function was given to me by my mentor Rory Ratrick Sheridan
def clear():
    """Clear function to clean-up the terminal so things don't get messy."""
    os.system("cls" if os.name == "nt" else "clear")
# End of borrowed code


def display_grid(name, player_grid, enemy_grid):
    """
    Generate the two battlegrids.

    it makes one for the player(left) and the enemy(right) based off
    the GAME_SIZE value.
    """
    print("")
    # 1st row
    frow = ("  ")
    for x in range(GAME_SIZE):
        frow = frow + f"| {x+1} "
    frow = frow + "|"
    print((GAME_SIZE*1)*" " + "Your Fleet" + (GAME_SIZE*3+2)*" " + frow)
    print((GAME_SIZE*4+4)*"-" + "   ||   " + (GAME_SIZE*4+4)*"-")

    # rows 2+
    for y in range(GAME_SIZE):
        row = "  "
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
    """
    Generate two random numbers.

    The numbers are between between 0 and 4 and put them into
    a dict to be used as coordinates.
    """
    coordinates = {"x": 0, "y": 0}
    coordinates["x"] = random.randrange(0, 5)
    coordinates["y"] = random.randrange(0, 5)
    return coordinates


def random_coordinates_x_gamesize(fleet):
    """
    Create 5 random cordinates.

    it will then use them as placement for the five ships on each side.
    """
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
    """Check cord against a cord_set to look for duplicates."""
    for existing_cord in cord_set:
        if cord["x"] == existing_cord["x"] and cord["y"] == existing_cord["y"]:
            return True


def replace_grid_cords(cords, grid, char):
    """Take the cordinates received in a dict format.

    Then updates the list item in the grid with the char(acter)
    """
    x = cords["x"]
    y = cords["y"]
    y_grid = grid[y]
    y_grid[x] = char


def show_player_fleet_on_grid(grid, fleet):
    """Take PLAYER_FLEET and changes the display on the grid."""
    global player_grid
    for cords in fleet:
        replace_grid_cords(cords, player_grid, Fore.GREEN+"@"+Fore.WHITE)


def enter_coordinates(player_shots):
    """Input two numbers and return a dict if valid."""
    coordinates = {"x": 0, "y": 0}
    while True:
        try:
            coordinates["x"] = int(
                                   input(
                                    "Place your shot along the X axis: \n"
                                        )
                                   ) - 1
            coordinates["y"] = int(
                                   input(
                                    "Place your shot along the Y axis: \n"
                                        )
                                   ) - 1
            if (
                coordinates["x"] < 0 or coordinates["x"] > 4
            ) or (
                coordinates["y"] < 0 or coordinates["y"] > 4
            ):
                print("Captain, these cordinates are invalid!" +
                      " Please enter cordinates between 1 and 5")
            elif coordinate_validation(coordinates, player_shots):
                print("Captain, we've already fired on this position!")
            else:
                break
        except ValueError:
            print("Captain,that's not even a number!" +
                  " Please enter cordinates between 1 and 5")
    return coordinates


def turn_retrieve_cordinates(shooter):
    """Generate the battle cordinates based on shooter.

    0 for player
    1 for enemy
    """
    global coordinates
    if shooter == 0:
        coordinates = enter_coordinates(player_shots)
    elif shooter == 1:
        while True:
            proposed_coordinates = random_coordinates()
            if coordinate_validation(proposed_coordinates, enemy_shots):
                continue
            else:
                coordinates = proposed_coordinates
                break


def turn_check_for_hit(coordinates, fleet, grid, player, shots):
    """
    Take the global cordinates and cycles through the fleet.

    it judges weither it's a hit or a miss.
    """
    hit_found = False
    for ship in fleet:
        if (coordinates["x"] == ship["x"]) and (coordinates["y"] == ship["y"]):
            fleet.remove(ship)
            if player == 0:
                print(
                    f"Success Captain {NAME}! You have hit an enemy ship!\n"
                      )
                global enemy_fleet
                enemy_fleet = fleet
            else:
                print(
                    f"Avast Captain {NAME}! They have hit a allied ship.\n"
                      )
                global player_fleet
                player_fleet = fleet
            hit_found = True
            replace_grid_cords(coordinates, grid, Fore.RED+"X"+Fore.WHITE)
            break
    if not hit_found:
        if player == 0:
            print(
                f"Miss Captain {NAME}, Your shot missed the enemy.\n"
                  )
        else:
            print(
                f"What fortune Captain {NAME}! Their shot missed us!\n"
                  )
        replace_grid_cords(coordinates, grid, "X")
    turn_add_to_shot_list(player, coordinates, shots)


def turn_add_to_shot_list(player, coordinates, shots):
    """Take the shot and adds it to a list."""
    global player_shots
    global enemy_shots
    shots.append(coordinates)
    if player == 0:
        player_shots = shots
    elif player == 1:
        enemy_shots = shots


if __name__ == "__main__":
    display_title()
    collect_name()
    random_coordinates_x_gamesize(1)
    random_coordinates_x_gamesize(2)
    show_player_fleet_on_grid(player_grid, player_fleet)
    display_grid(NAME, player_grid, enemy_grid)
    # this is the start the gameplay loop which keeps running
    # until one of thre three win conditions are true
    while (len(player_fleet)) > 0 and (len(enemy_fleet) > 0):
        turn_retrieve_cordinates(0)  # player input
        clear()  # This clears the terminal
        # Checks the player's shot for a hit
        turn_check_for_hit(
            coordinates, enemy_fleet, enemy_grid, 0, player_shots
                           )
        print("The enemy is returning fire!")
        turn_retrieve_cordinates(1)  # random computer input
        # Checks the enemy's shot for a hit
        turn_check_for_hit(
            coordinates, player_fleet, player_grid, 1, enemy_shots
                           )
        # Displays the grid once again with the updated values
        display_grid(NAME, player_grid, enemy_grid)
        if (len(player_fleet) == 0) and (len(enemy_fleet) == 0):
            print("The game has ended in a draw.")
        elif len(player_fleet) == 0:
            print("The game has ended in defeat.")
        elif len(enemy_fleet) == 0:
            print("The game has ended in victory!")

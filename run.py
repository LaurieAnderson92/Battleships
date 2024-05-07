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


def game_setup():
    game_size = input("Please select a number between 3 and 9 to determine the game size:\n")
        if game_size
    return game_size

display_title()
GAME_SIZE = game_setup()
print(f"starting a game with a size of {GAME_SIZE}")
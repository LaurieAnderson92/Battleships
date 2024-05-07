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
    game_size = int(game_size)
    try:
        if not 3 <= game_size < 9:
            raise ValueError(
                f"please enter number within the range 3-9, you provided {game_size}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")        
        
    return int(game_size)


display_title()
GAME_SIZE = game_setup()
print(f"starting a game with a size of {GAME_SIZE}")
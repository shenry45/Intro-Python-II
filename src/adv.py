from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ['stones', 'hammer', 'message']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(room['outside'], ['sword', 'belt'])

global game_active
game_active = True

def try_again():
    print('***Please try again.***')

def check_input(player1, user_input):
    if user_input == 'n':
        if hasattr(player1.current_room, 'n_to'):
            player1.current_room = player1.current_room.n_to
        else:
            try_again()
    elif user_input == 'e':
        if hasattr(player1.current_room, 'e_to'):
            player1.current_room = player1.current_room.e_to
        else:
            try_again()
    elif user_input == 's':
        if hasattr(player1.current_room, 's_to'):
            player1.current_room = player1.current_room.s_to
        else:
            try_again()
    elif user_input == 'w':
        if hasattr(player1.current_room, 'w_to'):
            player1.current_room = player1.current_room.w_to
        else:
            try_again()
    elif user_input == 'q':
        global game_active
        game_active = False
    else:
        print('Please enter a valid direction.')   
    
    # ITERATE THROUGH DIRECTIONS ATTEMPT

    # for val in directions:
    #     check_dir = exec(f'room[curr_room].{val}_to')

    #     if user_input == val:
    #         print('val matches')

    #         if check_dir:
    #             curr_player.current_room = check_dir
    #         else:
    #             print('***Please try again.***')



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while game_active:
    print(player1.current_room.name)
    print(player1.current_room.description)

    # Prints current items in room
    for item in player1.current_room.items:
        print(f'You see a %s' % (item))

    # Starts user input for movement
    user_input = input('Enter a cardinal direction (n, e, s, w): ')

    # checks user input and responsible for movement
    check_input(player1, user_input)
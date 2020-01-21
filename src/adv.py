from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# init items
sword = Item('sword', 'sharp stick')
stone = Item('stone', 'hardened earth')
message = Item('message', 'something scrolled but not legible, it looks quite old')

# assign items to rooms
room['outside'].items = [sword, stone, message]
room['treasure'].items = [message]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(room['outside'], [])

global game_active
game_active = True


# default return phrase
def try_again():
    print('***Please try again.*** \n')


# player item interaction
def item_interact(player, split_input):
    item_found = []

    # check if user wants to 'get' or 'take'
    if split_input[0] == 'get' or split_input[0] == 'take':
        # check if room has item user wants
        for item in player.current_room.items:
            # if item matches, remove from player inventory and add to room
            if item.name == split_input[1]:
                item_found.append(item)
                break

            else:
                pass
        
        if len(item_found) > 0:
            # add item to player inv
            item_found[0].on_take(player)
        else:
            pass

    # check if user wants to 'drop'
    elif split_input[0] == 'drop':
        # check if room has item user wants
        for item in player.inventory:
            # if item matches, remove from player inventory and add to room
            if item.name == split_input[1]:
                item_found.append(item)
                break

            else:
                pass
        
        if len(item_found) > 0:
            # add item to player inv
            item_found[0].on_drop(player)
        else:
            print(f'***You do not have {split_input[1]}*** \n')

    else:
        print('***Please enter a valid command.*** \n')


# checks player input and moves player
def check_input(player, user_input):
    split_input = user_input.split(' ')

    if len(split_input) == 2:
        item_interact(player, split_input)
    elif user_input == 'n':
        if hasattr(player.current_room, 'n_to'):
            player.current_room = player.current_room.n_to
        else:
            try_again()
    elif user_input == 'e':
        if hasattr(player.current_room, 'e_to'):
            player.current_room = player.current_room.e_to
        else:
            try_again()
    elif user_input == 's':
        if hasattr(player.current_room, 's_to'):
            player.current_room = player.current_room.s_to
        else:
            try_again()
    elif user_input == 'w':
        if hasattr(player.current_room, 'w_to'):
            player.current_room = player.current_room.w_to
        else:
            try_again()
    elif user_input == 'i':
        if len(player.inventory) > 0:
            print('Your inventory\n-----------')
            for item in player.inventory:
                print(item.name)
            print('\n')
        else:
            print('***You are carrying nothing.*** \n')

    elif user_input == 'q':
        global game_active
        game_active = False
    else:
        print('***Please enter a valid direction.*** \n')   
    
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
    print(player1.current_room.name, '--', player1.current_room.description)

    # Prints current items in room
    for item in player1.current_room.items:
        print(f'You see a %s' % (item.name))


    # Starts user input for movement
    user_input = input('Enter a cardinal direction (n, e, s, w): ')

    # checks user input and responsible for movement
    check_input(player1, user_input)

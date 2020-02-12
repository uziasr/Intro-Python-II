from room import Room
from player import Player
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

room['outside'].n_to = room['foyer']              #  5 rooms
room['foyer'].s_to = room['outside']              #                     
room['foyer'].n_to = room['overlook']             #    ___________________                 
room['foyer'].e_to = room['narrow']               #    _____|___os__|_____
room['overlook'].s_to = room['foyer']             #    ___n_|___f___|_____ 
room['narrow'].w_to = room['foyer']               #    ___t_|___ok__|_____
room['narrow'].n_to = room['treasure']            #         
room['treasure'].s_to = room['narrow']            #       

print(room['treasure']['s_to'])

player1 = Player('outside')
print(player1.room)

def start_game():
    valid_selections = ['n','w','s','e','q']
    player1 = Player('outside')
    while True:
        user_input = input('Please use N, S, W, E to travel across rooms, press Q to quit ').lower()
        if user_input in valid_selections:
            if player1.room=='outside':
                allowable_movements = {'s': room['outside']}
                if user_input in allowable_movements.keys():
                    player1.travel(allowable_movements[user_input].name)
            if player1.room=='foyer':
                allowable_movements = {'w','n','s'}
            if player1.room=='overlook':
                allowable_movements = ['n','w']
            if player1.room=='narrow':
                allowable_movements = ['s','e']
            if player1.room=='treasure':
                allowable_movements = ['n']
            print("You're currently in room {} you can't move {} from here".format(player1.room, user_input))
        else:
            print('Please use among the valid keys')


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

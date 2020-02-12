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
room['foyer'].e_to = room['narrow']               #    _____|___ok__|__t__
room['overlook'].s_to = room['foyer']             #    _____|___f___|__n__ 
room['narrow'].w_to = room['foyer']               #    _____|___os__|_____
room['narrow'].n_to = room['treasure']            #         
room['treasure'].s_to = room['narrow']            #       



def start_game():
    valid_selections = ['n','w','s','e']
    player1 = Player('Outside Cave Entrance')
    print('Welcome to the cave please navigate using keys: N, S, W, E, Q')
    while True:
        user_input = input('Where to (N,S,W,E,Q): ').lower()
        if user_input=='q':
            break
        elif user_input in valid_selections:
            if player1.room=='Outside Cave Entrance':
                allowable_movements = {'n': room['foyer']}
                if user_input in allowable_movements.keys():
                    new_room = allowable_movements[user_input]
                    print("\n{}\n{}\n".format(new_room.name, new_room.description ))
                    player1.travel(new_room.name)
                else:
                    print('You cant go that WAY, try {}'.format((' ').join(allowable_movements)) )
            elif player1.room=='Foyer':
                allowable_movements = {'n':room['overlook'],'s':room['outside'],'e':room['narrow']}
                if user_input in allowable_movements.keys():
                    new_room = allowable_movements[user_input]
                    print("\n{}\n{}\n".format(new_room.name, new_room.description ))
                    player1.travel(new_room.name)
                else:
                    print('You cant go that WAY, try {}'.format((' ').join(allowable_movements)) )
            elif player1.room=='Grand Overlook':
                allowable_movements = {'s':room['foyer']}
                if user_input in allowable_movements.keys():
                    new_room = allowable_movements[user_input]
                    print("\n{}\n{}\n".format(new_room.name, new_room.description ))
                    player1.travel(new_room.name)
                else:
                    print('You cant go that WAY, try {}'.format((' ').join(allowable_movements)) )
            elif player1.room=='Narrow Passage':
                allowable_movements = {'n':room['treasure'],'w':room['foyer']}
                if user_input in allowable_movements.keys():
                    new_room = allowable_movements[user_input]
                    print("\n{}\n{}\n".format(new_room.name, new_room.description ))
                    player1.travel(new_room.name)
                else:
                    print('You cant go that WAY, try {}'.format((' ').join(allowable_movements)) )
            elif player1.room=='Treasure Chamber':
                allowable_movements = {'s':room['narrow']}
                if user_input in allowable_movements.keys():
                    new_room = allowable_movements[user_input]
                    print("\n{}\n{}\n".format(new_room.name, new_room.description ))
                    player1.travel(new_room.name)
                else:
                    print('You cant go that WAY, try {}'.format((' ').join(allowable_movements)) )
                    # print("You're currently in room {} you can't move {} from here".format(player1.room, user_input))
        else:
            print('Please use among the valid keys')


start_game()
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

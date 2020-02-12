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
    
    def lead_the_way(user_input):
        valid_selections = ['n','w','s','e']
        combinations = {
            'Outside Cave Entrance':{'n': room['foyer']},
            'Foyer': {'n':room['overlook'],'s':room['outside'],'e':room['narrow']},
            'Grand Overlook': {'s':room['foyer']},
            'Narrow Passage': {'n':room['treasure'],'w':room['foyer']},
            'Treasure Chamber': {'s':room['narrow']}
            }
        if user_input in valid_selections:
            if user_input in combinations[player1.room].keys():
                new_room = combinations[player1.room][user_input]# Room Object!
                print("\n{}\n{}\n".format(new_room.name, new_room.description ))
                player1.travel(new_room.name)
            else:
                allowable_movements = combinations[player1.room].keys()
                print('You cant go that WAY, try {}'.format((', ').join(allowable_movements)))
        else:
                print('Please use a character among the valid keys')

    player1 = Player('Outside Cave Entrance')
    print('Welcome to the cave please navigate using keys: N, S, W, E, Q')
    while True:
        user_input = input('Where to (N,S,W,E,Q): ').lower()
        if user_input=='q':
            print('Good-bye Now!')
            break
        lead_the_way(user_input)
    

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

from room import Room
from player import Player
from items import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[Item('shield','looks to be made out of rune no less')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('sword','a dragon long sword, neat')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('bones', 'someone should probably bury these'),
 Item('water','a very refreshing sight to see'), Item('potion','This may heal my health or may poison me!')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('whip','This can kill a man')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('treasure', 'give me the loot!')]),
}


# Link rooms together

room['outside'].n_to = room['foyer']              #  5 rooms
room['foyer'].s_to = room['outside']              #                     
room['foyer'].n_to = room['overlook']             #    ___________________                 
room['foyer'].e_to = room['narrow']               #    _____|___ok_||__t__
room['overlook'].s_to = room['foyer']             #    _____|___f___|__n__ 
room['narrow'].w_to = room['foyer']               #    _____|___os__|_____
room['narrow'].n_to = room['treasure']            #         
room['treasure'].s_to = room['narrow']            #       


def lead_the_way(player, user_input):
    combinations = {
        'Outside Cave Entrance':{'n': room['foyer']},
        'Foyer': {'n':room['overlook'],'s':room['outside'],'e':room['narrow']},
        'Grand Overlook': {'s':room['foyer']},
        'Narrow Passage': {'n':room['treasure'],'w':room['foyer']},
        'Treasure Chamber': {'s':room['narrow']}
        }
    if user_input in combinations[player.room.name].keys():
        new_room = combinations[player.room.name][user_input]# Room Object!
        player.travel(new_room)
        print(player.room)
    else:
        allowable_movements = combinations[player.room.name].keys()
        print('You cant go that WAY, try {}'.format((', ').join(allowable_movements)))

def start_game():

    player1 = Player('Bill',room['outside'])
    valid_selections = ['n','w','s','e']
    action_selections = ['take', 'drop']

    print('Welcome to the cave please navigate using keys: N, S, W, E, Q')
    while True:
        user_input = input('Where to (N,S,W,E,Q): ').lower()
        if user_input=='q':
            print('Good-bye Now!')
            break
        elif user_input in valid_selections: 
            lead_the_way(player1, user_input)
        elif len(user_input.split(' ')) == 2:
            action = user_input.split(' ')[0]
            item = user_input.split(' ')[1]
            if action =='get':
                player1.take(item)
            elif action =='drop':
                player1.drop(item)
            else:
                print('valid commands only') 
        else:
            print(len(user_input.split(' ')), user_input[0])
            print("That isn't a valid key")
    

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

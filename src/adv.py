import sys
import time
import os
from room import Room
from player import Player
os.system("clear")

def Delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer",
                     "Dim light filters in from the south. Dusty passages run north and east."),

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print(Delay_print('\u001b[32mWelcome to Jack the Adventurer!!\u001b[0m'))

Jack = Player("Jack The adventurer", room['outside'], ['SCANNER', 'BACKPACK', 'WEAPON'])

# Write a loop that:
# print( Delay_print("You are currently in the " + Jack.active_room.name + ".\n" + Jack.active_room.description + "\n\n"))
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
def current_room(player):
    print( Delay_print("You are currently in the " + Jack.active_room.name + ".\n" + Jack.active_room.description + "\n\n"))
current_room(Jack)  
move = 0
while move != 'q':
    move = input('choose a direction N E S W: ')
    move = move.lower()
    if move == 'n':
        if(not hasattr(Jack.active_room, "n_to")):
            print('\nnothing to see here  go back to your track \n')
        else:
         Jack.active_room = Jack.active_room.n_to
         print(Delay_print("You have entered to the "" " +Jack.active_room.name+".\n"  + Jack.active_room.description + "\n\n" ))
    elif move == 'e':
        if(not hasattr(Jack.active_room,"e_to")):
            print(Delay_print('\nnothing to see here  go back to your track \n'))
        else:
            Jack.active_room = Jack.active_room.e_to
            print(Delay_print("You have entered to the "" " +Jack.active_room.name+".\n"  + Jack.active_room.description + "\n\n" ))
    elif move == 's':
        if(not hasattr(Jack.active_room,"s_to")):
            print(Delay_print('\nnothing to see here  go back to your track \n'))
        else: 
            Jack.active_room = Jack.active_room.s_to
            print(Delay_print("You have entered to the "" " +Jack.active_room.name+".\n"  + Jack.active_room.description + "\n\n" ))
    elif move == 'w':
        
        if(not hasattr(Jack.active_room,"w_to")):
            print(Delay_print('\nnothing to see here  go back to your track \n'))
        else: 
            Jack.active_room = Jack.active_room.w_to
            print(Delay_print("You have entered to the "" " +Jack.active_room.name+".\n"  + Jack.active_room.description + "\n\n" ))
    elif move == 'q':
        print("game over")  
    else: 
        print('PLEASE ENTER A VALID DIRECTION')
       
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#playerInput = ''

        # print(f'You just picked up a {playerInput}')
# If the user enters "q", quit the game.
from room import Room
from player import Player
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons" , 
    "__🁢_________________________⎧⎫‾‾‾‾‾‾"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""" , 
    "⎧⎫__🁢_____________________⎧⎫" ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""" , 
    "__🁢_________________________⎧⎫‾‾‾‾‾‾"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""" , 
    "__🁢_________________________⎧⎫‾‾‾‾‾‾"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""" , 
    "__🁢_________________________⎧⎫‾‾‾‾‾‾"),
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

# Main
# Make a new player object that is currently in the 'outside' room.

# START
os.system('clear')
print("    ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄\n   █░░░█░░░░░░░░░░▄▄░██░█\n   █░▀▀█▀▀░▄▀░▄▀░░▀▀░▄▄░█\n   █░░░▀░░░▄▄▄▄▄░░██░▀▀░█\n    ▀▄▄▄▄▄▀─────▀▄▄▄▄▄▄▀\n")
name = input( "What is your name, Adventurer?\n" )
player_one = Player( name , room[ "outside" ] )
quest_started = True
os.system('clear')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while quest_started:

    # FOR LOCATION

    adventurer_name = player_one.name
    current_room = player_one.current_room
    description = current_room.description
    picture = current_room.picture

    # CURRENT LOCATION
    print( picture )
    print( "\n" , "Current Location:" , current_room.name )
    print( " Description:" , description )
    print( "\n" ,  "Options:" )
    print( " N - North" , "S - South\n" , "E - East" , "W - West" , "\n" )

    # WHERE TO GO
    decision = input( " Where do you want to go?\n").lower()
    if decision is not None:

        if len( decision ) <= 1:

            # NORTH
            if decision[0] == "n":
                if current_room.n_to is not None:
                    os.system('clear')
                    # print( adventurer_name , "went North:\n" )
                    if player_one.current_room.name == "Outside Cave Entrance":
                        print("___🁢________________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___🁢________________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("____🁢_______________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("____🁢_______________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_____🁢______________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_____🁢______________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("______🁢_____________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("______🁢_____________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_______🁢____________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_______🁢____________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("________🁢___________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("________🁢___________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_________🁢__________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_________🁢__________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("__________🁢_________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("__________🁢_________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___________🁢________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___________🁢________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("____________🁢_______________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("____________🁢_______________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_____________🁢______________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_____________🁢______________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("______________🁢_____________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("______________🁢_____________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_______________🁢____________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_______________🁢____________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("________________🁢___________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("________________🁢___________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_________________🁢__________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_________________🁢__________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("__________________🁢_________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("__________________🁢_________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___________________🁢________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___________________🁢________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("____________________🁢_______⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("____________________🁢_______⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_____________________🁢______⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_____________________🁢______⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("______________________🁢_____⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("______________________🁢_____⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_______________________🁢____⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_______________________🁢____⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("________________________🁢___⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("________________________🁢___⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_________________________🁢__⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_________________________🁢__⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("__________________________🁢_⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("__________________________🁢_⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___________________________🁢⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___________________________🁢⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        player_one.current_room = current_room.n_to
                        continue
                    elif player_one.current_room.name == "Foyer":
                        print("⎧⎫___🁢____________________⎧⎫")
                        os.system('clear')
                        print("⎧⎫___🁢____________________⎧⎫")
                        os.system('clear')
                        print("⎧⎫____🁢___________________⎧⎫")
                        os.system('clear')
                        print("⎧⎫____🁢___________________⎧⎫")
                        os.system('clear')
                        print("⎧⎫_____🁢__________________⎧⎫")
                        os.system('clear')
                        print("⎧⎫_____🁢__________________⎧⎫")
                        os.system('clear')
                        print("⎧⎫______🁢_________________⎧⎫")
                        os.system('clear')
                        print("⎧⎫______🁢_________________⎧⎫")
                        os.system('clear')
                        print("⎧⎫_______🁢________________⎧⎫")
                        os.system('clear')
                        print("⎧⎫_______🁢________________⎧⎫")
                        os.system('clear')
                        print("⎧⎫________🁢_______________⎧⎫")
                        os.system('clear')
                        print("⎧⎫________🁢_______________⎧⎫")
                        os.system('clear')
                        print("⎧⎫_________🁢______________⎧⎫")
                        os.system('clear')
                        print("⎧⎫_________🁢______________⎧⎫")
                        os.system('clear')
                        print("⎧⎫__________🁢_____________⎧⎫")
                        os.system('clear')
                        print("⎧⎫__________🁢_____________⎧⎫")
                        os.system('clear')
                        print("⎧⎫___________🁢____________⎧⎫")
                        os.system('clear')
                        print("⎧⎫___________🁢____________⎧⎫")
                        os.system('clear')
                        print("⎧⎫____________🁢___________⎧⎫")
                        os.system('clear')
                        print("⎧⎫____________🁢___________⎧⎫")
                        os.system('clear')
                        print("⎧⎫_____________🁢__________⎧⎫")
                        os.system('clear')
                        print("⎧⎫_____________🁢__________⎧⎫")
                        os.system('clear')
                        print("⎧⎫______________🁢_________⎧⎫")
                        os.system('clear')
                        print("⎧⎫______________🁢_________⎧⎫")
                        os.system('clear')
                        print("⎧⎫_______________🁢________⎧⎫")
                        os.system('clear')
                        print("⎧⎫_______________🁢________⎧⎫")
                        os.system('clear')
                        print("⎧⎫________________🁢_______⎧⎫")
                        os.system('clear')
                        print("⎧⎫________________🁢_______⎧⎫")
                        os.system('clear')
                        print("⎧⎫_________________🁢______⎧⎫")
                        os.system('clear')
                        print("⎧⎫_________________🁢______⎧⎫")
                        os.system('clear')
                        print("⎧⎫__________________🁢_____⎧⎫")
                        os.system('clear')
                        print("⎧⎫__________________🁢_____⎧⎫")
                        os.system('clear')
                        print("⎧⎫___________________🁢____⎧⎫")
                        os.system('clear')
                        print("⎧⎫___________________🁢____⎧⎫")
                        os.system('clear')
                        print("⎧⎫____________________🁢___⎧⎫")
                        os.system('clear')
                        print("⎧⎫____________________🁢___⎧⎫")
                        os.system('clear')
                        print("⎧⎫_____________________🁢__⎧⎫")
                        os.system('clear')
                        print("⎧⎫_____________________🁢__⎧⎫")
                        os.system('clear')
                        print("⎧⎫______________________🁢_⎧⎫")
                        os.system('clear')
                        print("⎧⎫______________________🁢_⎧⎫")
                        os.system('clear')
                        print("⎧⎫_______________________🁢⎧⎫")
                        os.system('clear')
                        print("⎧⎫_______________________🁢⎧⎫")
                        os.system('clear')
                        player_one.current_room = current_room.n_to
                        continue
                    else:
                        player_one.current_room = current_room.n_to
                        continue
                else:
                    os.system('clear')
                    print( ". . . You can not go that way . . ." )
                    continue

            # SOUTH
            elif decision[0] == "s":
                if current_room.s_to is not None:
                    os.system('clear')
                    # print( adventurer_name , "went South:\n" )
                    if player_one.current_room.name == "Foyer":
                        print("___________________________🁢⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___________________________🁢⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("__________________________🁢_⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("__________________________🁢_⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_________________________🁢__⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_________________________🁢__⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("________________________🁢___⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("________________________🁢___⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_______________________🁢____⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_______________________🁢____⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("______________________🁢_____⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("______________________🁢_____⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_____________________🁢______⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_____________________🁢______⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("____________________🁢_______⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("____________________🁢_______⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___________________🁢________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___________________🁢________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("__________________🁢_________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("__________________🁢_________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_________________🁢__________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_________________🁢__________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("________________🁢___________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("________________🁢___________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_______________🁢____________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_______________🁢____________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("______________🁢_____________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("______________🁢_____________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_____________🁢______________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_____________🁢______________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("____________🁢_______________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("____________🁢_______________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___________🁢________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___________🁢________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("__________🁢_________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("__________🁢_________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_________🁢__________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_________🁢__________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("________🁢___________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("________🁢___________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_______🁢____________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_______🁢____________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("______🁢_____________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("______🁢_____________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_____🁢______________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("_____🁢______________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("____🁢_______________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("____🁢_______________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___🁢________________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        print("___🁢________________________⎧⎫‾‾‾‾‾‾")
                        os.system('clear')
                        player_one.current_room = current_room.s_to
                        continue
                    else:
                        os.system('clear')
                        player_one.current_room = current_room.s_to
                        continue
                else:
                    os.system('clear')
                    print( ". . . You can not go that way . . ." )
                    continue

            # EAST
            elif decision[0] == "e":
                if current_room.e_to is not None:
                    os.system('clear')
                    # print( adventurer_name , "went East:\n" )
                    player_one.current_room = current_room.e_to
                    continue
                else:
                    os.system('clear')
                    print( ". . . You can not go that way . . ." )
                    continue

            # WEST
            elif decision[0] == "w":
                if current_room.w_to is not None:
                    os.system('clear')
                    # print( adventurer_name , "went West:\n" )
                    player_one.current_room = current_room.w_to
                    continue
                else:
                    os.system('clear')
                    print( ". . . You can not go that way . . ." )
                    continue
            else:
                os.system('clear')
                print( ". . . Please try again . . ." )
                continue
    else:
        os.system('clear')
        print( ". . . Please try again . . ." )
        continue

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

from room import Room
import textwrap
import os

max_chars_per_line = 50
game_title = "Intro-Python-II"

# Methods


def print_game_title():
    str_stars_line = "*"*(max_chars_per_line-1)
    str_title_stars = "*"*(int(max_chars_per_line / 2) -
                           (2)-(int(len(game_title)/2)))
    print(str_stars_line)
    print(str_title_stars + " " + game_title + " " + str_title_stars)
    print(str_stars_line)


def console_print(str, max_chars_per_line):
    c_str = textwrap.wrap(str, max_chars_per_line)
    for line in c_str:
        print(line)


def print_commands_title():
    print("Commands:")


def print_command_quit():
    print("\tQuit:\t\"q\"")


def print_commands_move(moves):
    str_move_cmds = ""
    for move in moves:
        if move == "n":
            str_move_cmds += "\"n\" = move north    "
        elif move == "s":
            str_move_cmds += "\"s\" = move south    "
        elif move == "w":
            str_move_cmds += "\"w\" = move west    "
        elif move == "e":
            str_move_cmds += "\"e\" = move east    "
    print("\t" + "Moves:\t" + str_move_cmds)

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

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
room['outside'].set_moves(["n"])
room['foyer'].n_to = room['overlook']
room['foyer'].s_to = room['outside']
room['foyer'].e_to = room['narrow']
room['foyer'].set_moves(["n", "s", "e"])
room['overlook'].s_to = room['foyer']
room['overlook'].set_moves(["s"])
room['narrow'].n_to = room['treasure']
room['narrow'].w_to = room['foyer']
room['narrow'].set_moves(["n", "w"])
room['treasure'].s_to = room['narrow']
room['treasure'].set_moves(["s"])

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
current_room = room['outside']


os.system('cls' if os.name == 'nt' else 'clear')
print_game_title()
while True:
    print(current_room)
    print()
    print_commands_title()
    print_command_quit()
    print_commands_move(current_room.get_moves())
    print()
    cmd = input("Enter command:")
    if cmd == "q":
        break

os.system('cls' if os.name == 'nt' else 'clear')

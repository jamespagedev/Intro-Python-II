# ***********************************************************************
# ******************************* imports *******************************
# ***********************************************************************
import os
from room import Room
from player import Player

# ***********************************************************************
# ******************************* globals *******************************
# ***********************************************************************

max_chars_per_line = 50
game_title = "Intro-Python-II"
# order of possible_moves is coupled with logic in other file(s)
possible_moves = ["n", "s", "e", "w"]
move_north_index = 0
move_south_index = 1
move_east_index = 2
move_west_index = 3
room_keys = ['outside', 'foyer', 'overlook', 'narrow', 'treasure']

# ***********************************************************************
# ******************************* methods *******************************
# ***********************************************************************


def game_completed():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_game_title()
    print(
        f"Congradulations! You have found the {room_keys[len(room_keys) - 1]} room!!!")
    print()
    answer = input("Would you like to keep playing ([y]es, [n]o): ").lower()
    return answer == "n"

# ---------------------------- print methods ----------------------------


def print_game_title():
    str_stars_line = "*"*(max_chars_per_line-1)
    str_title_stars = "*"*(int(max_chars_per_line / 2) -
                           (2)-(int(len(game_title)/2)))
    print(str_stars_line)
    print(str_title_stars + " " + game_title + " " + str_title_stars)
    print(str_stars_line)


def print_player_items(player):
    if not player.get_items():
        print(f"{player} Items: None")
    else:
        print(f"{player} Items:")
        print("\tPrint list of items here")


def print_player_info(player):
    print(f"Character Name: {player}")
    print_player_items(player)


def print_commands_title():
    print("Commands:")


def print_command_quit():
    print("\t[q] = quits game")


def print_commands_move(moves):
    str_move_cmds = ""
    for move in moves:
        if move == possible_moves[move_north_index]:
            str_move_cmds += f"[{possible_moves[move_north_index]}] = move north    "
        elif move == possible_moves[move_south_index]:
            str_move_cmds += f"[{possible_moves[move_south_index]}] = move south    "
        elif move == possible_moves[move_east_index]:
            str_move_cmds += f"[{possible_moves[move_east_index]}] = move east    "
        elif move == possible_moves[move_west_index]:
            str_move_cmds += f"[{possible_moves[move_west_index]}] = move west    "
    print("\t" + str_move_cmds)

# ***********************************************************************
# ************************ Declare all the rooms ************************
# ***********************************************************************


dict_rooms = {
    room_keys[0]:  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    room_keys[1]:    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    room_keys[2]: Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    room_keys[3]:   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    room_keys[4]: Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# ***********************************************************************
# ************************* Link rooms together *************************
# ***********************************************************************

dict_rooms[room_keys[0]].n_to = dict_rooms[room_keys[1]]
dict_rooms[room_keys[0]].set_moves([possible_moves[move_north_index]])
dict_rooms[room_keys[1]].n_to = dict_rooms[room_keys[2]]
dict_rooms[room_keys[1]].s_to = dict_rooms[room_keys[0]]
dict_rooms[room_keys[1]].e_to = dict_rooms[room_keys[3]]
dict_rooms[room_keys[1]].set_moves([possible_moves[move_north_index],
                                    possible_moves[move_south_index],
                                    possible_moves[move_east_index]
                                    ])
dict_rooms[room_keys[2]].s_to = dict_rooms[room_keys[1]]
dict_rooms[room_keys[2]].set_moves([possible_moves[move_south_index]])
dict_rooms[room_keys[3]].n_to = dict_rooms[room_keys[4]]
dict_rooms[room_keys[3]].w_to = dict_rooms[room_keys[1]]
dict_rooms[room_keys[3]].set_moves([possible_moves[move_north_index],
                                    possible_moves[move_west_index]
                                    ])
dict_rooms[room_keys[4]].s_to = dict_rooms[room_keys[3]]
dict_rooms[room_keys[4]].set_moves([possible_moves[move_south_index]])

# ***********************************************************************
# ********************************* main ********************************
# ***********************************************************************

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

# game setup
os.system('cls' if os.name == 'nt' else 'clear')
print_game_title()
player_name = input("Enter character name: ")
player = Player(player_name)
current_room = dict_rooms[room_keys[0]]

# play game
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print_game_title()
    print_player_info(player)
    print()
    print(current_room)
    print()
    print_commands_title()
    print_command_quit()
    print_commands_move(current_room.get_moves())
    print()
    cmd = input("Enter command: ").lower()
    # quits game
    if cmd == "q":
        break
    # change room - valid move direction entered by user
    elif cmd in current_room.get_moves():
        current_room = current_room.next_room(cmd, possible_moves)
    # invalid move direction entered by user
    elif cmd in possible_moves:
        input("There is no room in that direction (press any key to continue...)")
    # input entered by user not recognized
    else:
        input("invalid command! (press any key to continue...)")
    # user beats game if in the final room
    if current_room.get_name() == dict_rooms[room_keys[len(room_keys) - 1]].get_name():
        if game_completed():
            break
os.system('cls' if os.name == 'nt' else 'clear')

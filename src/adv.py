# ***********************************************************************
# ******************************* imports *******************************
# ***********************************************************************
import os
from room import Room
from player import Player
from item import Item

# ***********************************************************************
# ******************************* globals *******************************
# ***********************************************************************

max_chars_per_line = 80
game_title = "Intro-Python-II"
# order of possible_moves is coupled with logic in other file(s)
possible_moves = ["n", "s", "e", "w"]
move_north_index = 0
move_south_index = 1
move_east_index = 2
move_west_index = 3
room_keys = ['outside', 'hidden', 'light',
             'foyer', 'overlook', 'narrow', 'treasure']

# ***********************************************************************
# ******************************* methods *******************************
# ***********************************************************************


def get_items_from_room(player_selected_itemnames, room, player):
    clear_screen()
    # First check if item(s) are in the room...
    # if not, return a message saying item "itemName" not found in current location
    for player_selected_itemname in player_selected_itemnames:
        if not room.is_item_in_room(player_selected_itemname):
            print(f"Item not found: {player_selected_itemname}")
            return input(f"(Press enter to continue...)")

    # Next remove the item(s) from the room and add to player item(s)
    player.add_items(room.get_items(player_selected_itemnames))

    # Finally, print the items (on player screen) removed from the room and stored with player
    print(f"{player} stores items: {player_selected_itemnames}")
    return input(f"(Press enter to continue...)")


def drop_items_in_room(player_selected_itemnames, player, room):
    clear_screen()
    # First check if player has item(s)...
    # if not, return a message saying item "itemName" not found in players inventory
    for player_selected_itemname in player_selected_itemnames:
        if player_selected_itemname not in player.get_item_names():
            print(
                f"Item not found in player inventory: {player_selected_itemname}")
            return input(f"(Press enter to continue...)")

    # Next remove the items(s) from player and add item(s) to room
    room.add_items(player.drop_items(player_selected_itemnames))

    # Finally, print the items (on player screen) that were dropped in the room
    print(f"{player} dropped items: {player_selected_itemnames}")
    return input(f"(press enter to continue...)")
# ---------------------------- print methods ----------------------------


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def game_completed():
    clear_screen()
    print_game_title()
    print(
        f"Congradulations! You have found the {room_keys[len(room_keys) - 1]} room!!!")
    print()
    answer = input("Would you like to keep playing ([y]es, [n]o): ").lower()
    return answer == "n"


def print_screen(room):
    clear_screen()
    print_game_title()
    print_player_info(player)
    print()
    print(current_room)
    print()
    print_room_items(room)
    print()
    print_commands_title()
    print_command_quit()
    print_command_inventory()
    print_commands_move(current_room.get_moves())
    print_commands_get_items()
    print_commands_take_items()
    print_commands_drop_items()
    print()


def print_game_title():
    str_stars_line = "*"*(max_chars_per_line-1)
    str_title_stars = "*"*(int(max_chars_per_line / 2) -
                           (2)-(int(len(game_title)/2)))
    print(str_stars_line)
    print(str_title_stars + " " + game_title + " " + str_title_stars)
    print(str_stars_line)


def display_inventory(player):
    clear_screen()
    print_player_items(player)
    print()
    input("Press enter to go exit inventory...")


def print_player_items(player):
    print(f"{player} Items:")
    items = player.get_items()
    if len(items) == 0:
        print("\tNone")
    else:
        line = "\t"
        for i in range(len(items)):
            # split line if the chars goes over max_chars_per_line
            if int(len(line)) + int(len(items[i].get_name())+9) > max_chars_per_line:
                line.strip()
                print(line)
                line = "\t"
            line += f"{i+1}. {items[i].get_name()}    "

        if line != "\t":
            print(line)


def print_player_info(player):
    print(f"Character Name: {player}")
    print_player_items(player)


def print_room_items(room):
    print("Items at Location:")
    items = room.get_items()
    if len(items) == 0:
        print("\tNone")
    else:
        line = "\t"
        for i in range(len(items)):
            # split line if the chars goes over max_chars_per_line
            if int(len(line)) + int(len(items[i].get_name())+9) > max_chars_per_line:
                line.strip()
                print(line)
                line = "\t"
            line += f"{i+1}. {items[i].get_name()}    "

        if line != "\t":
            print(line)


def print_commands_title():
    print("Commands:")


def print_command_quit():
    print("\t[q] = quits game")


def print_command_inventory():
    print("\t[i] = displays inventory")


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


def print_commands_get_items():
    print("\t[get item-name] = takes item(s) from room and adds to inventory. (example: [get sword potion shield])")


def print_commands_take_items():
    print("\t[take item-name] = same as [get item-name]")


def print_commands_drop_items():
    print("\t[drop item-name] = takes item(s) from inventory and leaves item(s) in current room. (example: [drop sword potion shield])")


def print_invalid_cmd(user_cmd):
    # invalid move direction entered by user
    if user_cmd in possible_moves:
        input("There is no room in that direction (press enter to continue...)")
    # input entered by user not recognized
    else:
        input("invalid command! (press enter to continue...)")


# ***********************************************************************
# ************************ Declare all the rooms ************************
# ***********************************************************************


dict_rooms = {
    room_keys[0]:  Room("Outside Cave Entrance", "North of you, the cave mount beckons", [Item("hp-potion", "refills hp"), Item("wooden-sword", "This weapon couldn't kill an elpy"), Item("wooden-armor", "Better than nothing!")]),

    room_keys[1]:    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. Something odd showing west""", [Item("hp-potion", "refills hp"), Item("iron-sword", "Bring on the big stuff!"), Item("iron-armor", "protects against claws and cuts")]),

    room_keys[2]:    Room("Hidden Passage", """Shining light to the north.""", []),

    room_keys[3]:    Room("Light Room", """WOW!!! It's bright in here!.""", [Item("LightSource", "May it shine light around you in dark times")]),

    room_keys[4]: Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("hp-full", "Restores hp to max"), Item("gold-sword", "Careful! It's sharp"), Item("gold-armor", "Protects against claws, cuts, and the ladies love it")]),

    room_keys[5]:   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("life", "revives upon death"), Item("master-sword", "Cuts through anything"), Item("master-armor", "Nearly invincible")]),

    room_keys[6]: Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("gold", "time to retire"), Item("will", "All your items will be handed to next player upon death")]),
}


# ***********************************************************************
# ************************* Link rooms together *************************
# ***********************************************************************

dict_rooms[room_keys[0]].n_to = dict_rooms[room_keys[1]]
dict_rooms[room_keys[0]].set_moves([possible_moves[move_north_index]])
dict_rooms[room_keys[1]].n_to = dict_rooms[room_keys[4]]
dict_rooms[room_keys[1]].s_to = dict_rooms[room_keys[0]]
dict_rooms[room_keys[1]].e_to = dict_rooms[room_keys[5]]
dict_rooms[room_keys[1]].w_to = dict_rooms[room_keys[2]]
dict_rooms[room_keys[1]].set_moves([possible_moves[move_north_index],
                                    possible_moves[move_south_index],
                                    possible_moves[move_east_index],
                                    possible_moves[move_west_index]
                                    ])
dict_rooms[room_keys[2]].n_to = dict_rooms[room_keys[3]]
dict_rooms[room_keys[2]].e_to = dict_rooms[room_keys[1]]
dict_rooms[room_keys[2]].set_moves([possible_moves[move_north_index],
                                    possible_moves[move_east_index]
                                    ])
dict_rooms[room_keys[3]].s_to = dict_rooms[room_keys[2]]
dict_rooms[room_keys[3]].set_moves([possible_moves[move_south_index]])
dict_rooms[room_keys[4]].s_to = dict_rooms[room_keys[1]]
dict_rooms[room_keys[4]].set_moves([possible_moves[move_south_index]])
dict_rooms[room_keys[5]].n_to = dict_rooms[room_keys[6]]
dict_rooms[room_keys[5]].w_to = dict_rooms[room_keys[1]]
dict_rooms[room_keys[5]].set_moves([possible_moves[move_north_index],
                                    possible_moves[move_west_index]
                                    ])
dict_rooms[room_keys[6]].s_to = dict_rooms[room_keys[5]]
dict_rooms[room_keys[6]].set_moves([possible_moves[move_south_index]])

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
clear_screen()
print_game_title()
player_name = input("Enter character name: ")
player = Player(player_name)
current_room = dict_rooms[room_keys[0]]

# play game
while True:
    # Prints information on the screen for the user to review
    print_screen(current_room)
    # user input = list[strings]...
    # --- replaces multiple whitespaces with one whitespace, and removes all leading/trailing whitespaces
    # --- sets all chars to lowercase
    # --- splits the chars/words into a list of strings (per whitespace in between them)
    cmd = ' '.join(input("Enter command: ").lower().split()).split(" ")
    # quits game
    if cmd[0] == "q":
        break
    # change room - valid move direction entered by user
    elif cmd[0] in current_room.get_moves():
        current_room = current_room.next_room(cmd[0], possible_moves)
    # show inventory
    elif cmd[0] == "i":
        display_inventory(player)
    # get item(s)
    elif "get" in cmd[0] or "take" in cmd[0]:
        get_items_from_room(cmd[1:], current_room, player)
    # drop item(s)
    elif "drop" in cmd[0]:
        drop_items_in_room(cmd[1:], player, current_room)
    # invalid cmd
    else:
        print('cmd =', f"\"{cmd[0]}\"")
        print_invalid_cmd(cmd[0])
    # user beats game if in the final room
    if current_room.get_name() == dict_rooms[room_keys[len(room_keys) - 1]].get_name():
        if game_completed():
            break
clear_screen()

# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.str_name = name
        self.str_description = description
        self.list_items_objects = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def get_name(self):
        return self.str_name

    def set_moves(self, moves):
        self.list_moves = moves

    def get_moves(self):
        return self.list_moves

    def get_items(self, user_itemnames=[]):
        if len(user_itemnames) == 0:
            return self.list_items_objects

        room_items_removed = []
        for user_itemname in user_itemnames:
            for item in self.list_items_objects:
                if item.get_name().lower() == user_itemname:
                    room_items_removed.append(self.list_items_objects.pop(
                        self.list_items_objects.index(item)))
                    break
        return room_items_removed

    def is_item_in_room(self, itemname):
        for item in self.list_items_objects:
            if itemname == item.get_name().lower():
                return True
        return False

    def additem(self, items):
        self.list_items_objects.extend(items)

    def next_room(self, usr_cmd, possible_moves):
        if usr_cmd == possible_moves[0]:
            return self.n_to
        elif usr_cmd == possible_moves[1]:
            return self.s_to
        elif usr_cmd == possible_moves[2]:
            return self.e_to
        elif usr_cmd == possible_moves[3]:
            return self.w_to

    def __str__(self):
        return f"Location: {self.str_name}\n\t{self.str_description}"

    def __repr__(self):
        return f"Location: {self.str_name}\n\t{self.str_description}"

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

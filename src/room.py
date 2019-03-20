# Implement a class to hold room information. This should have name and
# description attributes.
max_chars_per_line = 30


class Room:
    def __init__(self, name, description, items=[]):
        self.str_name = name
        self.str_description = description
        self.list_items_objects = items

    def set_moves(self, moves):
        self.list_moves = moves

    def get_moves(self):
        return self.list_moves

    def additem(self, items):
        self.list_items_objects.extend(items)
# code below from q&a

    def __str__(self):
        return f"Location: {self.str_name}\n\t{self.str_description}"

    def __repr__(self):
        return f"Location: {self.str_name}\n{self.str_description}"


room = Room("Office", "This is a regular looking office.", [])

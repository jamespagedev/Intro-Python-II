# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, items=[]):
        self.str_name = name
        self.list_items_objects = items

    def additem(self, item):
        self.list_items_objects.append(item)

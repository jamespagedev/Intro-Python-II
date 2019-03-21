# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, items=[]):
        self.str_name = name
        self.list_items_objects = items

    def __str__(self):
        return f"{self.str_name}"

    def add_items(self, items):
        for item in items:
            self.list_items_objects.append(item)

    def get_items(self):
        return self.list_items_objects

    def get_item_names(self):
        item_names = []
        for item in self.list_items_objects:
            item_names.append(item.get_name())
        return item_names

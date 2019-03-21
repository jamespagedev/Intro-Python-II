class Item:
    def __init__(self, name, description):
        # Precondition - name has only 1 word
        self.str_name = name
        self.str_description = description

    def get_name(self):
        return self.str_name

    def get_description(self):
        return self.str_description

    def __str__(self):
        return self.str_name

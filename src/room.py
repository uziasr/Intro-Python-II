# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
    def __getitem__(self, item):
        pass
    def __str__(self,):
        # print(self.items)
        current_items = (', ').join([i.name for i in self.items])
        if len(self.items) > 1:
            current_items = "It looks like there are {}\n".format((', ').join([i.name for i in self.items]))
        elif len(self.items)==1:
            current_items = "It looks like there is a {}\n".format((', ').join([i.name for i in self.items]))
        else:
            current_items=""
        return "\n{}\n{}\n{}".format(self.name, self.description, current_items)
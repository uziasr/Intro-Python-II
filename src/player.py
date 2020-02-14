# Write a class to hold player information, e.g. what room they are in
# currently.
from items import Item

class Player    :
    def __init__(self, name, room, inventory=[]):
        self.room = room
        self.inventory = inventory
    def travel(self, direction):
        self.room = direction
    def take(self, item):
        """takes in item as a string"""
        if item in [i.name for i in self.room.items]:
            item_obj = list(filter(lambda x: x.name==item,self.room.items))[0]
            item_obj.on_take()
            self.inventory.append(self.room.items.pop(self.room.items.index(item_obj)))
            print("You now have: {}".format(', '.join([item.name for item in self.inventory])))
        else:
            print("that item isn't in here")
    def drop(self, item):
        if item in [i.name for i in self.inventory]:
            item_obj = list(filter(lambda x: x.name==item,self.inventory))[0]
            item_obj.on_drop()
            item_index = self.inventory.index(item_obj)
            self.room.items.append(self.inventory.pop(item_index))
            print("You now have: {}".format(', '.join([item.name for item in self.inventory])))
        else:
            print('You that have that item, you got {}'.format(', '.join([item.name for item in self.inventory])))




        
    
        
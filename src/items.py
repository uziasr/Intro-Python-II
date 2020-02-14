class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self,):
        """This method is called when an item is picked up by the player"""
        """You have picked up [NAME]"""
        print ("You have picked up {}\n\n{}".format(self.name, self.description))
    def on_drop(self,):
        print ("You have dropped {}\n".format(self.name ))
        


# Write a class to hold player information, e.g. what room they are in
# currently.

# PLAYER INITIAL STATE
class Player:
    def __init__( self , name , current_room , backpack_equipped = False , items = [] ):
        self.name = name
        self.current_room = current_room
        self.backpack_equipped = backpack_equipped
        self.items = items

    # TAKE ITEM
    def take_item( self , item ):

        # EQUIP BACKPACK
        if item.name == "Backpack":
            self.backpack_equipped = True

        # MAKE USE OF BACKPACK
        if len( self.items ) <= 2 or self.backpack_equipped == True:
            self.items += item
            return True
        else:
            return False
    
    # REMOVE ITEM
    def remove_item( self , item ):

        # TAKE OFF BACKPACK
        if item.name == "Backpack":
            self.backpack_equipped = False
        
        # REMOVE ITEM
        for i in self.items:
            if i.name == item.name:
                self.items.remove( item )

        

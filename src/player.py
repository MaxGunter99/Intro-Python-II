# Write a class to hold player information, e.g. what room they are in
# currently.

# PLAYER INITIAL STATE
class Player:
    def __init__( self , name , current_room , lives , backpack_equipped = False , items = [] ):
        self.name = name
        self.current_room = current_room
        self.lives = lives
        self.backpack_equipped = backpack_equipped
        self.items = items

    # TAKE ITEM
    def take_item( self , item ):

        # EQUIP BACKPACK
        if item.name == "Backpack":
            self.backpack_equipped = True

        # MAKE USE OF BACKPACK
        elif self.backpack_equipped == True and item.name == "Key":
            self.items += item.name

        else:
            self.items += item.name
    
    # REMOVE ITEM
    def remove_item( self , item ):
        
        # REMOVE ITEM

        if item == "Key":
            self.item = ""
        
        # else:
        #     self.item -= item

        

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # player gets item
    def on_take(self, player):
        # add item to player inv
        player.inventory.append(self)
        
        # remove added inventory item from room
        player.current_room.items.remove(self)
    
        print(f'***You have picked up {self.name}.*** \n')

    # player drops item
    def on_drop(self, player):
        # remove item from player inv
        player.inventory.remove(self)

        # remove added inventory item from room
        player.current_room.items.append(self)

        print(f'***You dropped {self.name}.*** \n')

    
# Write a class to hold player information, e.g. what room they are in
# currently.

# Create player class
class Player:
    # inst attributes
    def __init__(self, current_room):
        # assign attributes to self
        self.current_room = current_room
# Implement a class to hold room information. This should have name and
# description attributes.

# create class
class Room:
    # create constructor with name & description
    def __init__(self, name, description, items):
        # tag self with attributes
        self.name = name
        self.description = description
        self.items = items
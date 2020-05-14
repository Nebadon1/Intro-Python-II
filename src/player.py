# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, active_room, inventory):
        self.name = name
        self.active_room = active_room
        self.inventory = inventory


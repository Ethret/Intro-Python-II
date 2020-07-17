# Write a class to hold player information, e.g. what room they are in
# currently.
class Explorer:
    def __init__(self, name, room, inventory=[]):
        self.name = name
        self.room = room
        self.inventory = inventory

player = Explorer("Adric", "Outside")
print(player.inventory)

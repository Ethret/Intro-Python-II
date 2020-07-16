import sys
from room import Room
from player import Explorer

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'death': Room("Death", """You died.""")
}




# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].n_to = room['death']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


name = input("Enter your name:")
p = Explorer(name, room["outside"])
message = ""

print("Welcome, " + name + ".")
print(p.room.name)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(f"You arrive at the {p.room.name}.")
    print(f"{p.room.description}")
    print(message)
    print("""Controls
        n: go north
        w: go west
        s: go south
        e: go east
        q: quit
    """)
    message = ""
    action = input(">> ")

    if action == 'n':
        if hasattr(p.room, 'n_to'):
            p.room = p.room.n_to
            if p.room == room['death']:
                print(f"You jump into the chasm. You die, {name}. Great job.")
                sys.exit()
        else:
            message = f"You can't go that way, {name}. Try again."

    elif action == 's':
        if hasattr(p.room, 's_to'):
            p.room = p.room.s_to
        else:
            message = f"You can't go that way, {name}. Try again."
    elif action == 'e':
        if hasattr(p.room, 'e_to'):
            p.room = p.room.e_to
        else:
            message = f"You can't go that way, {name}. Try again."
    elif action == 'w':
        if hasattr(p.room, 'w_to'):
            p.room = p.room.w_to
        else:
            message = f"You can't go that way, {name}. Try again."
    elif action == 'q':
        print("Goodbye.")
        sys.exit()
    else:
        message = f"Would you like to pick a valid selection, {name}?"

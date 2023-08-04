class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Central Corridor",
"""
This is the Central Corridor.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
This is the Laser Weapon Armory.
""")

the_bridge = Room("The Bridge",
"""
This is the Bridge.
""")

escape_pod = Room("Escape Pod",
"""
This is the Escape Pod.
""")

the_end_winner = Room("The End",
"""
You win!
""")

the_end_loser = Room("The End",
"""
The escape pod implodes.
""")

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

START = 'central_corridor'


def load_room(name):
    """
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)


def name_room(room):
    """
    Same possible security problem. Can you trust room?
    What's a better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key

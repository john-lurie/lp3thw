from unittest import TestCase

from gothonweb import planisphere as plan


class TestPlanisphere(TestCase):

    def test_room(self):
        gold = plan.Room("GoldRoom",
                         """This room has gold in it you can grab.
                         There's a door to the north.""")
        self.assertEqual(gold.name, "GoldRoom")
        self.assertEqual(gold.paths, {})

    def test_room_paths(self):
        center = plan.Room("Center", "Test room in the center.")
        north = plan.Room("North", "Test room in the north.")
        south = plan.Room("South", "Test room in the south.")

        center.add_paths({'north': north, 'south': south})
        self.assertEqual(center.go('north'), north)
        self.assertEqual(center.go('south'), south)

    def test_map(self):
        start = plan.Room("Start", "You can go west and down a hole.")
        west = plan.Room("Trees", "There are trees here, you can go east.")
        down = plan.Room("Dungeon", "It's dark down here, you can go up.")

        start.add_paths({'west': west, 'down': down})
        west.add_paths({'east': start})
        down.add_paths({'up': start})

        self.assertEqual(start.go('west'), west)
        self.assertEqual(start.go('west').go('east'), start)
        self.assertEqual(start.go('down').go('up'), start)

    def test_gothon_game_map(self):
        start_room = plan.load_room(plan.START)
        self.assertEqual(start_room.go('shoot!'), plan.generic_death)
        self.assertEqual(start_room.go('dodge!'), plan.generic_death)

        room = start_room.go('tell a joke')
        self.assertEqual(room, plan.laser_weapon_armory)

"""Study Drill 1:
Read about alternatives to nosetests.
This is important because the nosetests project is abandoned.

A test case is created by subclassing unittest.TestCase.

Run unittest from the top-level directory: "$ python -m unittest"
This will automatically find files matching test_*.py
"""
import unittest

from ex47.game import Room


class TestGame(unittest.TestCase):

    def test_room(self):
        gold = Room("GoldRoom",
                    """This room has gold in it you can grab. There's a
                    door to the north.""")
        self.assertEqual(gold.name, "GoldRoom")
        self.assertEqual(gold.paths, {})

    def test_room_paths(self):
        center = Room("Center", "Test room in the center.")
        north = Room("North", "Test room in the north.")
        south = Room("South", "Test room in the south.")

        center.add_paths({'north': north, 'south': south})
        self.assertEqual(center.go('north'), north)
        self.assertEqual(center.go('south'), south)

    def test_map(self):
        start = Room("Start", "You can go west and down a hole.")
        west = Room("Trees", "There are trees here, you can go east.")
        down = Room("Dungeon", "It's dark down here, you can go up.")

        start.add_paths({'west': west, 'down': down})
        west.add_paths({'east': start})
        down.add_paths({'up': start})

        self.assertEqual(start.go('west'), west)
        self.assertEqual(start.go('west').go('east'), start)
        self.assertEqual(start.go('down').go('up'), start)

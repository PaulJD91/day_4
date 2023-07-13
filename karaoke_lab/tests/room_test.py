import unittest
from src.rooms import Room
from src.guests import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_one = Room(1, 8)
        self.guest_1 = Guest("Merry")

    def test_check_in_guests(self):
        self.room_one.check_in_guests([self.guest_1])
        self.assertEqual(1, len(self.room_one.guests))

    def test_check_out_guest(self):
        self.room_one.check_in_guests([self.guest_1])
        self.room_one.check_out_guests([self.guest_1])
        self.assertEqual(0, len(self.room_one.guests))



import unittest
from src.person import Person

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person_1 = Person("Alice", 100)

    def test_add_to_list(self):
        self.person_1.add_to_list("apples")
        # self.assertEqual(1, len(self.person_1.shopping_list))
        self.assertEqual("appls", self.person_1.shopping_list[0])

    


    def test_remove_from_list(self):
        pass



    def test_print_shopping_list(shopping_list):
        pass
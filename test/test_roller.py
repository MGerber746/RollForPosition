import unittest
from rollerbot import position_roller as P

class TestRoller(unittest.TestCase):
    def test_roller_creation(self):
        people = ["banana", "ice cream", "apple"]
        roller = P.Roller(people)
        self.assertEqual(roller.people, people)

        self.assertEqual(len(roller.availableRolls), len(people))

        self.assertIn(P.Rolls(len(people)), roller.availableRolls)

        self.assertNotIn(P.Rolls(len(people) + 1), roller.availableRolls)

    def test_roll(self):
        people = ["banana", "ice cream", "apple"]
        roller = P.Roller(people)
        self.assertIsNotNone(roller.roll())


if __name__ == '__main__':
    unittest.main()

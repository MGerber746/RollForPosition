from enum import Enum
from itertools import islice
import random

class Rolls(Enum):
    CARRY = 1
    MID = 2
    OFFLANE = 3
    SOFT_SUPPORT = 4
    HARD_SUPPORT = 5


class Roller:
    def __init__(self, people):
        self.people = people
        self.availableRolls = set(islice(Rolls, 0, len(people)))

    def roll(self):
        assignedRolls = {}
        for person in self.people:
            currentRoll = random.choice(tuple(self.availableRolls))
            self.availableRolls.remove(currentRoll)
            assignedRolls[person] = currentRoll
        return assignedRolls

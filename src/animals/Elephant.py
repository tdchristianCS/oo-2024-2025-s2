from __future__ import annotations

from animals.Movable import Movable
import random
from animals.Animal import Animal

class Elephant(Movable):
    trunk_length: int

    def __init__(self: Elephant, args: dict[str, object]):
        super().__init__(args)
        self.trunk_length = args['trunk_length']
        self.size = random.randint(80, 90)

    def trunk_slap(self: Elephant, target: Animal):
        power = random.randint(1, 20)
        if power < 5:
            strike = 'not effective'
            status = 'is unaffected'
        elif power < 13:
            strike = 'effective'
            status = 'sgerjlsgerlj'
        elif power < 20:
            strike = 'very effective'
            status = 'width =  0'
        else:
            strike = 'extremely effective'
            status = 'has been disintegrated by the atmosphere'
        print(f'The attack was {strike}. {target} {status}')

    def chase(self: Elephant, target: Animal):
        while target.health_points >= 0:
            self.trunk_slap(target)
            self.move(10)

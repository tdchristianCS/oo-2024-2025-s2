from __future__ import annotations

from animals.Movable import Movable
import random
from animals.Animal import Animal
from foods.Food import Apple
from game.constants import TERRAIN_LAND

class Elephant(Movable):
    trunk_length: int
    speed = 25
    friendliness = 90
    diet = [Apple]
    size = 100

    def __init__(self: Elephant, args: dict[str, object]):
        """
        
        """
        args['fur_colour'] = 'grey'
        args['terrains'] = [TERRAIN_LAND]
        super().__init__(args)
        self.trunk_length = random.randint(10, 20)
        self.size = random.randint(80, 90)

        self.set_shared_info()

    def trunk_slap(self: Elephant, target: Animal):
        """
        set power to a random number between 1-20
        print attack effectiveness and target status depending on power
        """
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
        """
        call self.trunk_slap and self.move until the target health points equal 0
        """
        while target.health_points >= 0:
            self.trunk_slap(target)
            self.move(10)

    def format_info_lines(self: Elephant) -> list[str]:
        """
        Get lines from Animal and add trunk length to line
        """
        lines = super().format_info_lines()
        lines.extend([
            f'Trunk length: {self.trunk_length}'
        ])
        return lines
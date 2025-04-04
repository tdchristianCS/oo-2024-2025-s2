from __future__ import annotations
import random

from animals.Mammal import Mammal
from foods.Food import Apple
from game.constants import TERRAIN_WATER, TERRAIN_LAND


class Otter(Mammal):
    """
    An Otter is a type of Mammal that is intended to eat, move around,
    interact, die, etc. It is distinguished by its ability to travel on 
    water and land. It also tracks its wetness.
    """
    wetness_fatigue: int
    speed = 20
    size = 20
    friendliness = 30
    diet = [Apple]
    
    def __init__(self: Otter, args: dict[str, object]) -> None:
        """
        Create a new Otter. Set its default fur_colour and terrains.
        Also set a default wetness_fatigue that will be based on its
        movement over water and land.

        Expected args:
            - name
            - gender
        """

        args['fur_colour'] = 'brown'
        args['terrains'] = [TERRAIN_WATER, TERRAIN_LAND]
        super().__init__(args)
        self.wetness_fatigue = 0
        
        self.set_shared_info()

    def move(self: Otter, duration: int) -> None:
        """
        Swim.
        """
        self.swim(duration)

    def swim(self: Otter, duration: int) -> None:
        """
        Swim for the given duration.
        If the otter is too wet, based on the wetness fatigue, then it won't
        be allowed into the water. Othewise, it will be allowed into the water
        and the exaustion/wetness fatigue will be updated.
        """
        if self.wetness_fatigue > 90:
            print(f'{self.name} too tired of being wet; needs to dry off Currently at {self.wetness_fatigue}% humid.')

        else:
            tiredness_factor = random.randint(3, 20)

            self.wetness_fatigue += duration * tiredness_factor
            if self.wetness_fatigue > 100:
                self.wetness_fatigue = 100

            print(f'{self.name} swam for {duration} seconds. New wetness fatigue: {self.wetness_fatigue}%')

    def format_info_lines(self: Otter) -> list[str]:
        """
        Return a list of strings containing info about this Otter.
        """
        lines = super().format_info_lines()
        lines.extend([
            f'Fur: {self.fur_colour}'
        ])
        return lines

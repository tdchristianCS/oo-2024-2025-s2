from __future__ import annotations
import random

from animals.Mammal import Mammal
from foods.Food import Apple
from game.constants import TERRAIN_WATER, TERRAIN_LAND


class Otter(Mammal):
    wetness_fatigue: int
    speed = 20
    size = 20
    friendliness = 30
    diet = [Apple]
    
    def __init__(self: Otter, args: dict[str, object]) -> None:
        args['fur_colour'] = 'brown'
        args['terrains'] = [TERRAIN_WATER, TERRAIN_LAND]
        super().__init__(args)
        self.wetness_fatigue = 0
        
        self.set_shared_info()


    def move(self: Otter, duration: int) -> None:
        self.swim(duration)

    def swim(self: Otter, duration: int) -> None:
        if self.wetness_fatigue > 90:
            print(f'{self.name} too tired of being wet; needs to dry off Currently at {self.wetness_fatigue}% humid.')

        else:
            tiredness_factor = random.randint(3, 20)

            self.wetness_fatigue += duration * tiredness_factor
            if self.wetness_fatigue > 100:
                self.wetness_fatigue = 100

            print(f'{self.name} swam for {duration} seconds. New wetness fatigue: {self.wetness_fatigue}%')

    def format_info_lines(self: Cat) -> str:
        return [
            f'{self.name} ({self.age} {self.gender})',
            f'Fur: {self.fur_colour}',
            f'Diet: {self.diet}'
        ]    

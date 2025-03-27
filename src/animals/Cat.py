from __future__ import annotations
import random

# from the Mammal module import the Mammal class
from animals.Mammal import Mammal
from foods.Food import Meat
from game.constants import TERRAIN_LAND

class Cat(Mammal):
    fur_colour: str
    luck: bool
    friendliness = 50
    speed = 40
    size = 30
    diet = [Meat]

    def __init__(self: Cat, args: dict[str, object]) -> None:
        args['terrains'] = [TERRAIN_LAND]
        super().__init__(args)

        if self.fur_colour == 'black':
            self.luck = 10
        else:
            self.luck = 50

        self.set_shared_info()
        self.info['fur_colour'] = self.fur_colour
        self.info['luck'] = self.luck

    def move(self: Cat, duration: int) -> None:
       self.walk(duration)

    def walk(self: Cat, duration: int) -> None:

        # TODO Cat walk duration is not used :(

        # With luck, 3/4 chances to walk
        # No luck, 1/9 chances to walk
        if self.luck:
            success = random.randint(1, 4) < 3
        else:
            success = random.randint(1, 9) < 2
        
        if success:
            print(f'{self.name} is walking')
        else:
            if self.gender == 'M':
                pronoun = 'himself'
            else:
                pronoun = 'herself'

            print(f'{self.name} tripped on {pronoun}')
    
    def format_info_lines(self: Cat) -> list[str]:
        return [
            f'{self.name} ({self.age} {self.gender})',
            f'Fur: {self.fur_colour}',
            f'Diet: {self.diet}',
            f'Luck: {self.luck}',
        ]

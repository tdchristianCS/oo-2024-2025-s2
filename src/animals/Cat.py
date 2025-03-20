from __future__ import annotations
import random

# from the Mammal module import the Mammal class
from animals.Mammal import Mammal
from foods.Food import Meat

class Cat(Mammal):
    fur_colour: str
    luck: bool

    def __init__(self: Cat, name: str, gender: str, fur_colour: str, luck: int) -> None:
        super().__init__(name, gender, fur_colour)
        self.luck = luck

        self.friendliness = 50
        self.speed = 40
        self.size = 30
        self.diet = [Meat]

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
    
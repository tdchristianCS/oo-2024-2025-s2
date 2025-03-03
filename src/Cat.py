from __future__ import annotations
import random

# from the Mammal module import the Mammal class
from Mammal import Mammal

class Cat(Mammal):
    fur_colour: str
    luck: bool

    def __init__(self: Cat, name: str, gender: str, fur_colour: str) -> None:
        super().__init__(name, gender)

        self.fur_colour = fur_colour

        # We can do some logic with a DERIVED attribute!!
        if self.fur_colour == 'BLACK':
            self.luck = False
        else:
            self.luck = True
        
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
    
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

        self.friendliness = 50
        self.speed = 40
        self.size = 30
        self.diet = [Meat]

    @staticmethod
    def make_random() -> Cat:

        fur_colours = []
        names = []

        with open('src/data/cat.txt', 'r') as f:
            for line in f.readlines():
                line = line.strip()

                if line.startswith(';'):
                    continue
                if not line:
                    continue

                parts = line.split('::')

                if parts[0] == 'fur_colour':
                    fur_colour = parts[1]

                    if len(parts) == 3:
                        luck = parts[2]
                    else:
                        luck = 50

                    fur_colours.append([fur_colour, luck])
                
                elif parts[0] == 'name':
                    name = parts[1]

                    if len(parts) == 3:
                        gender = parts[2]
                    else:
                        gender = random.choice(['M', 'F'])

                    names.append([name, gender])
        
        fur_colour, luck = random.choice(fur_colours)
        name, gender = random.choice(names)

        return Cat(name, gender, fur_colour, luck)

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
    
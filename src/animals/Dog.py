from __future__ import annotations
import random

# from the Mammal module import the Mammal class
from animals.Mammal import Mammal
from foods.Food import Meat
from game.constants import TERRAIN_LAND

class Dog(Mammal):
    loudness_bark: int
    lung_capacity: int
    diet = [Meat]

    def __init__(self: Dog, args: dict[str, object]) -> None:
        args['terrains'] = [TERRAIN_LAND]
        super().__init__(args)
        
        # self.lung_capacity = 0
        # self.lung_capacity = random.randint(0,50)
        # self.lung_capacity = random.randint(0, 50)

        self.set_shared_info()
        self.info['fur_colour'] = self.fur_colour

    def move(self: Dog, duration: int) -> None:
        self.walk(duration)

    def walk(self: Dog, duration: int) -> None:

        if self.lung_capacity < 0:
            self.lung_capacity = 0
        elif self.lung_capacity > 100:
            self.lung_capacity = 100

        while self.lung_capacity > (20+duration):
            print(f'{self.name} is walking')
            self.lung_capacity -= 10
            
        else:
            print(f'{self.name} is too tired to walk')

    def format_info_lines(self: Dog) -> list[str]:
        lines = super().format_info_lines()
        lines.extend([
            f'Fur: {self.fur_colour}',
            f'Lung capacity: {self.lung_capacity}'
        ])
        return lines

class Husky(Dog):
    lung_capacity = 75
    friendliness = 70
    speed = 70
    size = 35

    def __init__(self: Husky, args: dict[str, object]) -> None:
        args['fur_colour'] = 'grey'
        super().__init__(args)

class Chihuahua(Dog):
    lung_capacity = 30 
    friendliness = 90
    speed = 100
    size = 20

    """
    From data: name, gender
    Supplied: fur_colour
    """
    def __init__(self: Chihuahua, args: dict[str, object]) -> None:
        args['fur_colour'] = 'beige'
        super().__init__(args)

class Mutt(Dog):
    lung_capacity = 50
    friendliness = 10
    speed = 10
    size = 30

    """
    From data: name, gender, fur_colour
    """
    def __init__(self: Mutt, args: dict[str, object]) -> None:
        super().__init__(args)

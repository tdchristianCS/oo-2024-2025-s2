from __future__ import annotations
import random

# from the Mammal module import the Mammal class
from animals.Mammal import Mammal
from foods.Food import Meat

class Dog(Mammal):
    loudness_bark: int

    def __init__(self: Dog, args: dict[str, object]) -> None:
        super().__init__(args)
        self.lung_capacity = random.randint(0, 50)

        self.friendliness = 80
        self.speed = 50
        self.size = 50
        self.diet = [Meat]

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
    

class Husky(Dog):
    def __init__(self: Husky, args: dict[str, object]) -> None:
        args['fur_colour'] = 'grey'
        super().__init__(args)
        self.lung_capacity = 50


class Chihuahua(Dog):
    def __init__(self: Chihuahua,  args: dict[str, object]) -> None:
        args['fur_colour'] = 'beige'
        super().__init__(args)
        self.lung_capacity -= 30 

class Mutt(Dog):
    def __init__(self: Mutt,  args: dict[str, object]) -> None:
        super().__init__(args)


from __future__ import annotations
import random

# from the Mammal module import the Mammal class
from Mammal import Mammal


class Dog(Mammal):
    breed: str
    loudness_bark: int

    def __init__(self: Dog, name: str, gender: str, fur_colour: str) -> None:
        super().__init__(name, gender, fur_colour)
        self.lung_capacity = 0
        self.lung_capacity = random.randint(0,50)

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
    def __init__(self: Husky, name:str, gender:str) -> None:
        super().__init__(name, gender)
        self.breed = 'Husky'
        self.lung_capacity = 50


class Chihauhua(Dog):
    def __init__(self: Chihauhua, name:str, gender:str) -> None:
        super().__init__(name, gender)
        self.breed = 'Chihuahua'
        self.lung_capacity -= 30 

class Mutt(Dog):
    def __init__(self: Mutt, name:str, gender:str) -> None:
        super().__init__(name, gender)
        self.breed = 'mutt' 


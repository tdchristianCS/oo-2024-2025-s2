from __future__ import annotations
import random

from animals.Mammal import Mammal
from foods.Food import Meat, Apple

class Rodent(Mammal):
    diseases: list[str]
    has_tail: bool
    
    def __init__(self: Rodent, name: str, gender: str, fur_colour: str) -> None:
        super().__init__(name, gender, fur_colour)

        self.diseases = []

    ##def move(self: Rodent, duration: int) -> None:

class Rat(Rodent):
    def __init__(self: Rodent, name: str, gender: str, fur_colour: str) -> None:
        super().__init__(name, gender, fur_colour)


        self.friendliness = 5
        self.speed = 15
        self.size = 10
        self.diet = [Meat, Apple]

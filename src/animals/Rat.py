from __future__ import annotations
import random

from animals.Rodent import Rodent
from foods.Food import Apple

class Rat(Rodent):

    def __init__(self: Rat, name: str, gender: str, fur_colour: str) -> None:
        super().__init__(name, gender, fur_colour)

        self.friendliness = 0
        self.speed = 5
        self.size = 5
        self.diet = [Apple]

    def move(self: Rat, duration: int) -> None:
        self.walk(duration)

    def walk(self: Rat, duration: int) -> None:
        print(f'{self.name} walked for {duration} seconds.')

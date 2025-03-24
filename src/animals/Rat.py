from __future__ import annotations
import random

from animals.Rodent import Rodent
from foods.Food import Apple

class Rat(Rodent):

    def __init__(self: Rat, args: dict[str, object]) -> None:
        super().__init__(args)

        self.friendliness = 0
        self.speed = 5
        self.size = 5
        self.diet = [Apple]
        self.has_tail = True
        
        self.set_shared_info()

    def move(self: Rat, duration: int) -> None:
        self.walk(duration)

    def walk(self: Rat, duration: int) -> None:
        print(f'{self.name} walked for {duration} seconds.')

from __future__ import annotations
import random

from animals.Rodent import Rodent
from foods.Food import Apple

class Rat(Rodent):
    friendliness = 0
    speed = 5
    size = 15
    diet = [Apple]
    
    def __init__(self: Rat, args: dict[str, object]) -> None:
        super().__init__(args)

        self.has_tail = True
        
        self.set_shared_info()

    def move(self: Rat, duration: int) -> None:
        self.walk(duration)

    def walk(self: Rat, duration: int) -> None:
        print(f'{self.name} walked for {duration} seconds.')

    def format_info_lines(self: Rat) -> list[str]:
        return [
            f'{self.name} ({self.age} {self.gender})',
            f'Friendliness: {self.friendliness}',
            f'Diet: {self.format_diet()}',
            f'Size: {self.size}',
        ]
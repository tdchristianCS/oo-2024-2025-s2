from __future__ import annotations
import random

from animals.Rodent import Rodent
from foods.Food import Apple

class Rat(Rodent):
    """
    Friendliness is set to zero, very unfriendly.
    Speed is set to 5, quite fast.
    Size is set to 15, quite small.
    Diet is set to just apple for now.
    """
    friendliness = 0
    speed = 5
    size = 15
    diet = [Apple]
    
    def __init__(self: Rat, args: dict[str, object]) -> None:
        """
        Gets properties from "Rodent" class and sets has_tail to true.
        """
        super().__init__(args)

        self.has_tail = True
        
        self.set_shared_info()

    def move(self: Rat, duration: int) -> None:
        self.walk(duration)
        """
        Gets move property from "Movable" class and calls the walk function
        """

    def walk(self: Rat, duration: int) -> None:
        print(f'{self.name} walked for {duration} seconds.')
        """
        Takes the rat name and duration and prints a sentence. 'Rodent walked for 10 seconds.'
        """
    def format_info_lines(self: Rat) -> list[str]:
        """
        Formats attributes into readable text when mousing over a rat.
        """
        lines = super().format_info_lines()
        lines.extend([
            f'Fur: {self.fur_colour}',
            f'Diseases: {self.diseases}'
        ])
        return lines
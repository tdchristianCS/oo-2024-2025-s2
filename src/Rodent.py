from __future__ import annotations
import random

from Mammal import Mammal

class Rodent(Mammal):
    diseases: list[str]
    fur_colour: str
    has_tail: bool
    size: int
    diet: list[str]
    
    def __init__(self: Rodent, name: str, gender: str, fur_colour: str, size: int, diet: list[str]) -> None:
        super().__init__(name, gender)

        self.diseases = []
        self.fur_colour = fur_colour
        self.size = size
        self.diet = diet

    ##def move(self: Rodent, duration: int) -> None:

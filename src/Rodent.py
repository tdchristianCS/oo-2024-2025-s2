from __future__ import annotations
import random

from Mammal import Mammal

class Rodent(Mammal):
    diseases: list[str]
    has_tail: bool
    
    def __init__(self: Rodent, name: str, gender: str, fur_colour: str, size: int, diet: list[str]) -> None:
        super().__init__(name, gender, fur_colour)

        self.diseases = []

    ##def move(self: Rodent, duration: int) -> None:

from __future__ import annotations
import random

from animals.Mammal import Mammal
from foods.Food import Meat, Apple

class Rodent(Mammal):
    diseases: list[str]
    has_tail: bool
    
    def __init__(self: Rodent, args: dict[str, object]) -> None:
        super().__init__(args)

        self.diseases = []

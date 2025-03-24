from __future__ import annotations
import random

from animals.Mammal import Mammal
from foods.Food import Meat, Apple
from game.constants import TERRAIN_LAND

class Rodent(Mammal):
    diseases: list[str]
    has_tail: bool
    
    def __init__(self: Rodent, args: dict[str, object]) -> None:
        args['terrains'] = [TERRAIN_LAND]
        
        super().__init__(args)
        
        self.diseases = []

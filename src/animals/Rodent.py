from __future__ import annotations
import random

from animals.Mammal import Mammal
from foods.Food import Meat, Apple
from game.constants import TERRAIN_LAND

class Rodent(Mammal):
    """
    Defines Rodent. 
    Rodents are filthy, so this gives them a diseases list of strings.
    Some have tails, so we have a bool for has_tail.
    """
    diseases: list[str]
    has_tail: bool
    
    def __init__(self: Rodent, args: dict[str, object]) -> None:
        """
        Acts as a parent class for all rodents.
        """
        args['terrains'] = [TERRAIN_LAND]
        
        super().__init__(args)
        
        self.diseases = []

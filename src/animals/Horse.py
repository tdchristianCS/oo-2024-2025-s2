from __future__ import annotations 
from animals.Equine import Equine
import random

from foods.Food import Apple

class Horse(Equine): 
    can_lock_legs: bool     #true :), so they don't fall while sleeping 
    hunger_pct: int 
    memory_capability: int
    # Assuming that we can measure this on sonme sort of scale where different
    # sides: 0 being Dory Level --> 100 being MEGA MIND MEMORY 
    # (cause horses are big brain??)

    def __init__(self: Horse, args: dict[str, object]) -> None:
        super().__init__(args)

        self.friendliness = 80
        self.speed = 70
        self.size = 110
        self.diet = [Apple]




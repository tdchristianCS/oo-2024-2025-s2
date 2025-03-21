from animals.Animal import Animal
from animals.Equine import Equine
from __future__ import annotations
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

    def move(self: Horse, duration: int) -> None:
       self.walk(duration) 
    def walk(self: Horse, duration: int) -> None:
    
    def energy(self: Horse) -> None: 
        pass 
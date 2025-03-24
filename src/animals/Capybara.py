from __future__ import annotations
import random

from animals.Rodent import Rodent
from foods.Food import Apple
from game.constants import TERRAIN_WATER, TERRAIN_LAND

class Capybara(Rodent):
   
    swim_energy_meter: int

    def __init__(self: Capybara, args: dict[str, object]) -> None:
        args['terrains'] = [TERRAIN_WATER, TERRAIN_LAND]
        
        super().__init__(args)
        self.swim_energy_meter = 100

        self.friendliness = 100
        self.speed = 25
        self.size = 25
        self.diet = [Apple]
        self.has_tail = False

        self.set_shared_info()

    def move(self: Capybara, duration: int) -> None:
        self.swim(duration)

    def swim(self: Capybara, duration: int) -> None:
        tiredness_factor = random.randint(1, 2)

        duration_swam = duration

        self.swim_energy_meter -= duration * tiredness_factor
        if self.swim_energy_meter < 0:
            # we ran out of energy, so we deduct frmo duration_swam

            duration_swam -= duration / tiredness_factor
            self.swim_energy_meter = 0

        print(f'{self.name} swam for {duration_swam} seconds. The swim energy meter is {self.swim_energy_meter}.')

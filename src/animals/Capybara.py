from __future__ import annotations
import random

from animals.Rodent import Rodent
from foods.Food import Apple

class Capybara(Rodent):
    friendliness = 100
    speed = 25
    size = 25
    diet = [Apple]
    

    def __init__(self: Capybara, args: dict[str, object]) -> None:
        super().__init__(args)
        self.swim_energy_meter = 100

       
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

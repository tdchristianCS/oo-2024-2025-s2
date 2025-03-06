from __future__ import annotations
import random

from animals.Rodent import Rodent
from foods.Food import Apple

class Capybara(Rodent):
   
    swim_energy_meter: int

    def __init__(self: Capybara, name: str, gender: str, fur_colour: str) -> None:
        super().__init__(name, gender, fur_colour)
        self.swim_energy_meter = 100

        self.friendliness = 100
        self.speed = 25
        self.size = 25
        self.diet = [Apple]

    def move(self: Capybara, duration: int) -> None:
        self.swim(duration)

    def swim(self: Capybara, duration: int) -> None:
        tiredness_factor = random.randint(1, 2)

        durationSwam = duration

        self.swim_energy_meter -= duration * tiredness_factor
        if self.swim_energy_meter < 0:
            # we ran out of energy, so we deduct frmo durationSwam

            durationSwam -= duration / tiredness_factor
            self.swim_energy_meter = 0

        print(f'{self.name} swam for {durationSwam} seconds. The swim energy meter is {self.swim_energy_meter}.')



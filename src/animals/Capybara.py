from __future__ import annotations
import random

from animals.Rodent import Rodent
from foods.Food import Apple

class Capybara(Rodent):
    """
    Capybaras have no tail and can swim. Their diet consists of apples
    and they're very friendly.
    """
    friendliness = 100
    speed = 25
    size = 25
    diet = [Apple]

    def __init__(self: Capybara, args: dict[str, object]) -> None:
        """
        Set has_tail to False.
        Also set the energy meter for swimming.
        """
        super().__init__(args)
        self.swim_energy_meter = 100

        self.has_tail = False

        self.set_shared_info()

    def move(self: Capybara, duration: int) -> None:
        """Swim."""
        self.swim(duration)

    def swim(self: Capybara, duration: int) -> None:
        """
        Take a duration and deduct the energy meter based on that duration.
        If the energy meter goes below zero, the Capybara will not continue.
        """
        tiredness_factor = random.randint(1, 2)

        duration_swam = duration

        self.swim_energy_meter -= duration * tiredness_factor
        if self.swim_energy_meter < 0:
            # we ran out of energy, so we deduct frmo duration_swam

            duration_swam -= duration / tiredness_factor
            self.swim_energy_meter = 0

        print(f'{self.name} swam for {duration_swam} seconds. The swim energy meter is {self.swim_energy_meter}.')

    def format_info_lines(self: Capybara) -> list[str]:
        """
        Return a list of strings containing info about this Otter.
        """
        return [
            f'{self.name} ({self.age} {self.gender})',
            f'Fur: {self.fur_colour}',
            f'Diet: {self.diet}'
            f'Friendliness: {self.friendliness}'
        ]
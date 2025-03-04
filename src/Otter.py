from __future__ import annotations
import random

from Mammal import Mammal

class Otter(Mammal):
    wetness_fatigue: int
    
    def __init__(self: Otter, name: str, gender: str) -> None:
        super().__init__(name, gender)
        self.wetness_fatigue = 0

    def move(self: Otter, duration: int) -> None:
        self.swim(duration)

    def swim(self: Otter, duration: int) -> None:
        if self.wetness_fatigue > 90:
            print(f'{self.name} too tired of being wet; needs to dry off Currently at {self.wetness_fatigue}% humid.')

        else:
            tiredness_factor = random.randint(3, 20)

            self.wetness_fatigue += duration * tiredness_factor
            if self.wetness_fatigue > 100:
                self.wetness_fatigue = 100

            print(f'{self.name} swam for {duration} seconds. New wetness fatigue: {self.wetness_fatigue}%')

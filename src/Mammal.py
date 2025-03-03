from __future__ import annotations

from Movable import Movable

class Mammal(Movable):

    def __init__(self: Mammal, name: str, gender: str) -> None:

        # This is one of those lines to just learn :(
        # It means use the parent (Animal)'s init method
        # In other words, the Animal handles the name and gender
        super().__init__(name, gender)
        self.n_legs = 4

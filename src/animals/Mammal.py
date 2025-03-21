from __future__ import annotations

from animals.Movable import Movable

class Mammal(Movable):
    n_legs: int
    fur_colour: str

    def __init__(self: Mammal, args: dict[str, object]) -> None:

        # This is one of those lines to just learn :(
        # It means use the parent (Animal)'s init method
        # In other words, the Animal handles the name and gender
        super().__init__(args)
        self.fur_colour, _ = args['fur_colour']
        
        self.n_legs = 4

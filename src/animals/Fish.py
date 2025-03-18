from __future__ import annotations

from animals.Movable import Movable

class Fish(Movable):

    def __init__(self: Fish, name: str, gender: str, colour: str) -> None:

        # This is one of those lines to just learn :(
        # It means use the parent (Animal)'s init method
        # In other words, the Animal handles the name and gender
        super().__init__(name, gender)
        self.n_fins = 6

    def move(self: Fish, duration: int) -> None: 
        self.move(duration)
    
   
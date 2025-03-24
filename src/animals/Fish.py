from __future__ import annotations

from animals.Movable import Movable
from game.constants import TERRAIN_WATER

class Fish(Movable):

    def __init__(self: Fish, args: dict[str, object]) -> None:
        args['terrains'] = [TERRAIN_WATER]
        super().__init__(args)
        self.n_fins = 6

    def move(self: Fish, duration: int) -> None: 
        self.move(duration)
    
from __future__ import annotations
from game.assets import assets

class Entity:
    image: object
    info: dict[str, object]
    terrains: list[str]
    
    def __init__(self: Entity, args: dict[str, object]) -> None:
        self.terrains = args['terrains']
        self.set_image()
        self.info = {}

    def set_image(self: Entity) -> None:
        my_class = str(type(self).__name__).lower()
        self.image = assets[my_class]

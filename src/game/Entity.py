from __future__ import annotations
from game.assets import assets

class Entity:
    image: object
    info: dict[str, object]
    
    def __init__(self: Entity) -> None:
        self.set_image()
        self.info = {}

    def set_image(self: Entity) -> None:
        my_class = str(type(self).__name__).lower()
        self.image = assets[my_class]

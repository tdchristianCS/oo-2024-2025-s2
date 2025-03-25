from __future__ import annotations
from game.assets import assets

import pygame

BASE_SIZE_FACTOR = 100

class Entity:
    image: object
    info: dict[str, object]
    terrains: list[str]
    
    def __init__(self: Entity, args: dict[str, object]) -> None:
        self.terrains = args['terrains']
        self.set_image()
        self.info = {}

    def set_image(self: Entity) -> None:
        cl_ = type(self)
        key = str(cl_.__name__).lower()
        key_scaled = f'{key}_scaled'

        if key_scaled not in assets:
            image = assets[key]
            scaled_image = pygame.transform.scale_by(image, cl_.size / BASE_SIZE_FACTOR)
            assets[key_scaled] = scaled_image
        self.image = assets[key_scaled]

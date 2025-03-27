from __future__ import annotations
from game.assets import assets

import pygame
import math

BASE_SIZE_FACTOR = 60
COLLAPSE_FACTOR = 1.5

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
            # factor = (cl_.size + (abs(50 - cl_.size) ** 0.25)) / BASE_SIZE_FACTOR
            # factor = cl_.size / BASE_SIZE_FACTOR
            # factor = (cl_.size + ((50 - cl_.size) / COLLAPSE_FACTOR)) / BASE_SIZE_FACTOR
            factor = ((0.0004*(cl_.size - 50) ** 3) + 50)/100
            scaled_image = pygame.transform.scale_by(image, factor)
            assets[key_scaled] = scaled_image
        self.image = assets[key_scaled]

    def format_info_lines(self: Entity) -> list[str]:
        return[""]
    
    def update(self: Entity) -> None:
        """Set age to the number of seconds passed."""
        self.age = pygame.time.get_ticks() // 1_000
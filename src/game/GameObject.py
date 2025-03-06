from __future__ import annotations

from game.Point import Point
from game.Entity import Entity

class GameObject:
    point: Point
    image: object
    rect: object
    entity: Entity

    def __init__(self: GameObject, entity: Entity, point: Point) -> None:
        self.animal, self.point = entity, point
        self.image = self.entity.image
        self.rect = None

    def draw(self: GameObject, surface: object) -> None:
        self.rect = surface.blit(self.image, (self.point))
    
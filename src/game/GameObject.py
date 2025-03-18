from __future__ import annotations
import pygame.transform

from game.Point import Point
from game.Entity import Entity

class GameObject:
    point: Point
    image: object
    rect: object
    entity: Entity

    def __init__(self: GameObject, entity: Entity, point: Point) -> None:
        self.entity, self.point = entity, point
        self.image = self.entity.image

        self.image = pygame.transform.scale_by(self.image, 0.5 + (self.entity.size / 100))

        self.rect = None

    def draw(self: GameObject, surface: object) -> None:
        self.rect = surface.blit(self.image, (self.point))

    def draw_hitbox(self: GameObject, surface: object) -> None:
        pygame.draw.rect(surface, '#ff00ff', self.rect, 2)
    
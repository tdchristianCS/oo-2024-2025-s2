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

        w = self.image.get_width()
        h = self.image.get_height()
        x = point.x
        y = point.y
        self.rect = pygame.Rect(x - w, y - h, w, h)

    def draw(self: GameObject, surface: object) -> None:
        x, y = self.point.x, self.point.y
        tl_x = x - (self.image.get_width() / 2)
        tl_y = y - (self.image.get_height() / 2)
        self.rect = surface.blit(self.image, (tl_x, tl_y))

    def draw_hitbox(self: GameObject, surface: object) -> None:
        pygame.draw.rect(surface, '#ff00ff', self.rect, 2)

    def draw_info(self: GameObject, surface: object, font: object) -> None:
        text = font.render(self.entity.info['name'], False, (255, 255, 255))
        w = self.image.get_width()
        h = self.image.get_height()
        surface.blit(text, (self.point.x - (w / 2), (self.point.y + (h / 2))))
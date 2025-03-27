from __future__ import annotations
import pygame

from game.Point import Point
from game.Entity import Entity

LINE_SPACING = 2
STROKE_WIDTH = 2

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
        lines = self.entity.format_info_lines()

        for i in range(len(lines)):
            line = lines[i]

            text_under = font.render(line, False, (0, 0, 0))
            text_over = font.render(line, False, (255, 255, 255))
            x = self.rect.left
            y = self.rect.bottom + LINE_SPACING + ((text_over.get_height() + LINE_SPACING) * i)
            surface.blit(text_under, (x, y + STROKE_WIDTH))
            surface.blit(text_under, (x, y - STROKE_WIDTH))
            surface.blit(text_under, (x + STROKE_WIDTH, y))
            surface.blit(text_under, (x - STROKE_WIDTH, y))
            surface.blit(text_over, (x, y))

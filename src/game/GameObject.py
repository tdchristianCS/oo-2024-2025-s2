from __future__ import annotations
import pygame

from game.Point import Point
from game.Entity import Entity

from game.assets import tr_60

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

    def draw_info_bg(self: GameObject, surface: object, font: object) -> None:
        lines = self.entity.format_info_lines()

        w_biggest = 0

        rendered_lines = []
        for line in lines:
            rendered = font.render(line, False, (255, 255, 255))
            rendered_lines.append(rendered)
            w = rendered.get_width()
            if w_biggest < w:
                w_biggest = w

        h_overall = LINE_SPACING + ((rendered_lines[0].get_height() + LINE_SPACING) * len(lines))

        bg_scaled = pygame.transform.scale(tr_60, (w_biggest, h_overall))
        surface.blit(bg_scaled, self.rect.bottomleft)

        for i in range(len(rendered_lines)):
            rendered = rendered_lines[i]

            x = self.rect.left
            y = self.rect.bottom + LINE_SPACING + ((rendered.get_height() + LINE_SPACING) * i)
            surface.blit(rendered, (x, y))

    def update(self: GameObject) -> None:
        self.entity.update()
        
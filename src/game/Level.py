from __future__ import annotations
import pygame

class Level:
    rect: pygame.Rect
    water_rects: list
    obstacle_rects: list

    def __init__(self: Level, name: str, image: object) -> None:
        self.name, self.image = name, image
        self.water_rects = []
        self.obstacle_rects = []
        self.rect = None

        self.read_data()

    def read_data(self: Level) -> None:
        with open(f'src/data/levels/{self.name}.txt', 'r') as f:
            for line in f.readlines():
                line = line.strip()

                if line.startswith(';'):
                    continue
                if not line:
                    continue

                parts = line.split('::')
                kind = parts[0]
                tl, br = parts[1:]
                left, top = tl.split(',')
                right, bottom = br.split(',')

                rect = pygame.Rect(int(left), int(top), int(right) - int(left), int(bottom) - int(top))

                if kind == 'water':
                    self.water_rects.append(rect)
                
                elif kind == 'obstacle':
                    self.obstacle_rects.append(rect)

    def draw(self: Level, surface: object) -> None:
        self.rect = surface.blit(self.image, (0, 0))

    def draw_water(self: Level, surface: object) -> None:
        for rect in self.water_rects:
            pygame.draw.rect(surface, '#0066ff', rect)

from __future__ import annotations
import pygame

class Level:
    water_rects: list
    obstacle_rects: list

    def __init__(self: Level, name: str, image: object) -> None:
        self.name, self.image = name, image
        self.water_rects = []
        self.obstacle_rects = []

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
                tl, tr, bl, br = parts[1:]
                rect = pygame.Rect(tl_x)



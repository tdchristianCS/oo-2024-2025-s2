from __future__ import annotations

from game.Point import Point

class GameObject:
    point: Point
    image: object
    rect: object

    def __init__(self: GameObject, point: Point, image: object) -> None:
        self.point, self.image = point, image
        self.rect = None
        
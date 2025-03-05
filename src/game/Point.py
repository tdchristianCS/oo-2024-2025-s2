from __future__ import annotations

class Point:
    x: int
    y: int

    def __init__(self: Point, x: int, y: int) -> None:
        self.x, self.y = x, y

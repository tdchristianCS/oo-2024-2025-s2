from __future__ import annotations

class Food:
    name: str
    hp_added: int

class Apple(Food):
    def __init__(self: Apple) -> None:
        super().__init__()
        self.name = 'Apple'
        self.hp_added = 5

class Meat(Food):
    def __init__(self: Meat) -> None:
        super().__init__()
        self.name = 'Meat'
        self.hp_added = 10

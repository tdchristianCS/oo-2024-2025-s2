from __future__ import annotations

from game.Entity import Entity
from foods.Food import Food

class Animal(Entity):
    age: int        # This is in seconds
    name: str
    gender: str
    n_legs: int
    # IQ: int         
    friendliness: int
    speed: int
    # stubborness: int 
    # domesticablity_pct: int
    size: float
    diet: list[Food]
    can_ride: bool
    image: object

    def __init__(self: Animal, name: str, gender: str) -> None:
        super().__init__()
        # First we create the attributes that came from arguments
        self.name = name
        self.gender = gender

        # Then we set the attributes that have default values
        self.age = 0

        # For n_legs, there may be no default value that makes sense
        # It is OK for this to have no value; it will cause an error
        # if someone tries to access it, which is OK.

        # Default
        self.can_ride = False

from __future__ import annotations
import random

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
        self.info = {}

    def set_shared_info(self: Animal) -> None:
        self.info = {
            'name': self.name,
            'gender': self.gender,
            'size': self.size,
            'speed': self.speed,
            'friendliness': self.friendliness,
            'diet': self.diet   
        }

    @staticmethod
    def make_random(_class) -> Animal:

        fur_colours = []
        names = []

        key = _class.__name__.lower()

        with open(f'src/data/animals/{key}.txt', 'r') as f:
            for line in f.readlines():
                line = line.strip()

                if line.startswith(';'):
                    continue
                if not line:
                    continue

                parts = line.split('::')

                if parts[0] == 'fur_colour':
                    fur_colour = parts[1]

                    if len(parts) == 3:
                        luck = parts[2]
                    else:
                        luck = 50

                    fur_colours.append([fur_colour, luck])
                
                elif parts[0] == 'name':
                    name = parts[1]

                    if len(parts) == 3:
                        gender = parts[2]
                    else:
                        gender = random.choice(['M', 'F'])

                    names.append([name, gender])
        
        fur_colour, luck = random.choice(fur_colours)
        name, gender = random.choice(names)

        return _class(name, gender, fur_colour, luck)

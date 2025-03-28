from __future__ import annotations
import random

from game.Entity import Entity
from foods.Food import Food

import pygame

class Animal(Entity):
    birth_age: int
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

    def __init__(self: Animal, args: dict[str, object]) -> None:
        """
        Expected args:
          name: str
          gender: str
        """
        super().__init__(args)

        # First we create the attributes that came from arguments
        self.name, self.gender = args['name']

        # Then we set the attributes that have default values
        self.birth_age = pygame.time.get_ticks()
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
    def make_random_animal(_class: type) -> Animal:
        # TODO All animals of the same species have the same name :(((

        arg_choices = {'name': []}

        key = _class.__name__.lower()

        with open(f'src/data/animals/{key}.txt', 'r') as f:
            for line in f.readlines():
                line = line.strip()

                if line.startswith(';'):
                    continue
                if not line:
                    continue

                parts = line.split('::')

                if parts[0] == 'name':
                    name = parts[1]

                    if len(parts) == 3:
                        gender = parts[2]
                    else:
                        gender = random.choice(['M', 'F'])

                    arg_choices['name'].append([name, gender])
                
                else:                    

                    key = parts[0]
                    if len(parts) > 2:
                        value = parts[1:]
                    else:
                        value = parts[1]
                    
                    if key not in arg_choices:
                        arg_choices[key] = []
                    
                    arg_choices[key].append(value)
                
        # Choose randomly from the choices        
        args = {}
        for key in arg_choices:
            args[key] = random.choice(arg_choices[key])

        return _class(args)

    def format_diet(self: Animal) -> str:
        return 'Diet: ' + ', '.join(cl_.__name__ for cl_ in self.diet)
    
    def format_friendliness(self: Animal) -> str:
        return f'<3  {self.friendliness}'
    
    def format_speed(self: Animal) -> str:
        return f'>>  {self.speed}'
    
    def format_size(self: Animal) -> str:
        return f'++  {self.size}'
    
    def format_info_lines(self: Animal) -> str:
        return [
            f'{self.name} ({self.gender} {self.age})',
            f'{self.format_friendliness()}  |  {self.format_speed()}  |  {self.format_size()}',
            self.format_diet()
        ]

    def update(self: Animal) -> bool:
        """
        Update this Animal.
        - Set age to the number of seconds passed.
        - TEST If age >= 10, the animal dies.

        Return True iff the Animal is still alive at the end of the update.
        """
        self.age = (pygame.time.get_ticks() - self.birth_age) // 1_000
        return self.age < random.randint(8, 12)        

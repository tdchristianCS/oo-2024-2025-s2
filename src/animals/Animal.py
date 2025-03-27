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
        # TODO increase age with every second?
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
        return '🍕' + ', '.join(cl_.__name__ for cl_ in self.diet)
    
    def format_friendliness(self: Animal) -> str:
        return f'❤️ {self.frendliness}'
    
    def format_speed(self: Animal) -> str:
        return f'⏩ {self.speed}'
    
    def format_size(self: Animal) -> str:
        return f'🪐 {self.size}'
    
    def format_gender(self: Animal) -> str:
        if self.gender == 'M':
            return '♂'
        elif self.gender == 'F':
            return '♀'
    
    def format_info_lines(self: Animal) -> str:
        return [
            f'{self.name} ({self.format_gender()} {self.age})',
            f'{self.format_size()} {self.format_speed()} {self.format_size()}',
            self.format_diet()
        ]

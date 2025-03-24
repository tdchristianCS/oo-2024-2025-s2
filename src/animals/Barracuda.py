from __future__ import annotations
import random

from animals.Fish import Fish 
from foods.Food import Meat

class Barracuda(Fish):
    n_fish_eaten: int 
    size_of_shark: int 
    n_teeth: int

    def __init__(self: Barracuda, args: dict[str, object]) -> None:
        super().__init__(args)

        self.size = 2
        self.speed = 50
        self.friendliness = 5
        self.diet = [Meat]

        self.n_fish_eaten = 0
        n_teeth_options = [140, 150, 160, 170, 180, 190, 200, 210, 220]
        self.n_teeth = random.choice(n_teeth_options)

        self.set_shared_info()
    
    def swim(self: Barracuda, duration: int) -> None: 
        if self.size > 10: 
            self.n_fish_eaten == 20 

        elif self.size < 10: 
            self.n_fish_eaten = 10
            print(f'{self.name} has ate {self.n_fish_eaten}. They must now swim to burn the calories!!! ')

        else: 
            appetite = random.randint(1, 10)
            
            self.n_fish_eaten += duration * appetite
            if self.n_fish_eaten > 20:
                self.n_fish_eaten < 10 

                print(f'{self.name} swam for {duration} seconds. The current fish eaten: {self.n_fish_eaten}int' )

        n_teeth_options = [140, 150, 160, 170, 180, 190, 200, 210, 220]
        self.n_teeth = random.choice(n_teeth_options)

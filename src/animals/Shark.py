from __future__ import annotations
import random

from animals.Fish import Fish 
from foods.Food import Meat


class Shark(Fish):
    n_fish_eaten: int 
    size: int 

    def __init__(self: Shark, args: dict[str, object]) -> None:
        super().__init__(args)
      

        self.size = 5
        self.speed = 60
        self.friendliness = 10
        self.diet = [Meat]

        self.n_fish_eaten = 0        
        
        self.set_shared_info()
    
    def swim(self: Shark, duration: int) -> None: 
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

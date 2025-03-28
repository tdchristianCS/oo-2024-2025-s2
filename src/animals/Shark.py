from __future__ import annotations
import random

from animals.Fish import Fish 
from foods.Food import Meat


class Shark(Fish):
    n_fish_eaten: int 
    size: int 
    size = 80
    speed = 60
    friendliness = 10
    diet = [Meat]
    n_fish_eaten = 0     

    def __init__(self: Shark, args: dict[str, object]) -> None:
        super().__init__(args)
      
        """
        Expected ARGS's : 
        name 
        gender
        """
     

        self.set_shared_info()
    
    def swim(self: Shark, duration: int) -> None:
        """
        Eat fish based on the Shark's size and the swim duration.
        """
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
    
    def format_info_lines(self: Shark) -> str:
        """
        Gives information on the shark
        """        
        lines = super().format_info_lines()
        lines.extend([
            f'Fish eaten: {self.n_fish_eaten}'
        ])
        return lines
     
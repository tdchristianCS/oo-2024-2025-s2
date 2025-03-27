from __future__ import annotations
import random

from animals.Fish import Fish 
from foods.Food import Meat

class Barracuda(Fish):
    
    n_fish_eaten: int 
    size: int 
    teeth_options = [140, 150, 160, 170, 180, 190, 200, 210, 220]
    n_teeth: int
    luck: bool

    size = 30
    speed = 50
    friendliness = 5
    diet = [Meat]

    def __init__(self: Barracuda, args: dict[str, object]) -> None:
        super().__init__(args)

        self.n_fish_eaten = 0
        self.n_teeth = random.choice(self.teeth_options)
        self.luck = random.randint(1, 5)

        self.set_shared_info()

    def swim(self: Barracuda, duration: int) -> None: 
        if self.size > 2: 
            self.n_fish_eaten == 10 

        elif self.size < 2: 
            self.n_fish_eaten == 5
            print(f'{self.name} has ate {self.n_fish_eaten}. They must now swim to burn the calories!!! ')

        else: 
            appetite = random.randint(1, 10)
            
            self.n_fish_eaten += duration * appetite
            if self.n_fish_eaten > 20:
                self.n_fish_eaten < 10 

                print(f'{self.name} swam for {duration} seconds. The current fish eaten: {self.n_fish_eaten}int' )

        if self.n_fish_eaten == 10:
            self.luck = False 
        else: 
            self.luck = True

            if self.luck == False: 
                self.n_teeth - 10 
                print(f'{self.name} has ate {self.n_fish_eaten} and has lost ten teeth -> {self.n_teeth}.')

                #else:
                    # self.nteeth - 0 <- woulnt this work too? 

            elif self.luck == True:
                self.n_teeth - 0 
                    
                print(f'{self.name} has ate {self.n_fish_eaten} with this amount of teeth -> {self.n_teeth}.')

    def format_info_lines(self: Barracuda) -> list[str]:
        return [
            f'{self.name} ({self.age} {self.gender})',
            f'Teeth: {self.n_teeth}',
            f'Diet: {self.format_diet()}',
            f'Luck: {self.luck}'
        ]

if __name__ == '__main__':
    b = Barracuda('LOL', 'F')
    b.swim(5)   

    
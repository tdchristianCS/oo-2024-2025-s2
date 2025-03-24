from __future__ import annotations
import random

from animals.Fish import Fish 
from foods.Food import Meat

class Barracuda(Fish):
    
    number_of_fish_eaten: int 
    size_of_Barracuda: int 
    List_of_teeth = [140, 150, 160, 170, 180, 190, 200, 210, 220]
    n_teeth = random.choice(List_of_teeth)
    luck: bool 


    def __init__(self: Barracuda, name: str, gender: str) -> None:
        super().__init__(name, gender, 'grey')
        self.number_of_fish_eaten = 0
        self.size_of_Barracuda= 2

    
    def swim(self: Barracuda, duration: int) -> None: 
        if self.size_of_Barracuda > 2: 
            self.number_of_fish_eaten == 10 

        elif self.size_of_Barracuda < 2: 
            self.number_of_fish_eaten == 5
            print(f'{self.name} has ate {self.number_of_fish_eaten}. They must now swim to burn the calories!!! ')

        else: 
            appetite = random.randint(1, 10)
            
            self.number_of_fish_eaten += duration * appetite
            if self.number_of_fish_eaten > 20:
                self.number_of_fish_eaten < 10 

                print(f'{self.name} swam for {duration} seconds. The current fish eaten: {self.number_of_fish_eaten}int' )

        if self.number_of_fish_eaten == 10:
            self.luck = False 
        else: 
            self.luck = True

            if self.luck == False: 
                self.n_teeth - 10 
                print(f'{self.name} has ate {self.number_of_fish_eaten} and has lost ten teeth -> {self.n_teeth}.')

                #else:
                    # self.nteeth - 0 <- woulnt this work too? 

            elif self.luck == True:
                self.n_teeth - 0 
                    
                print(f'{self.name} has ate {self.number_of_fish_eaten} with this amount of teeth -> {self.n_teeth}.')

b = Barracuda('LOL', 'F')
b.swim(5)
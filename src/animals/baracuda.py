from __future__ import annotations
import random

from animals.Fish import Fish 


class Barracuda(Fish):
    number_of_fish_eaten: int 
    size_of_shark: int 

    def __init__(self: Barracuda, name: str, gender: str) -> None:
        super().__init__(name, gender, 'grey')
        self.number_of_fish_eaten = 0
        self.size_of_Barracuda= 2
    
    def swim(self: Barracuda, duration: int) -> None: 
        if self.size_of_Barracuda > 10: 
            self.number_of_fish_eaten == 20 

        elif self.size_of_Barracuda < 10: 
            self.number_of_fish_eaten = 10
            print(f'{self.name} has ate {self.number_of_fish_eaten}. They must now swim to burn the calories!!! ')

        else: 
            appetite = random.randint(1, 10)
            
            self.number_of_fish_eaten += duration * appetite
            if self.number_of_fish_eaten > 20:
                self.number_of_fish_eaten < 10 

                print(f'{self.name} swam for {duration} seconds. The current fish eaten: {self.number_of_fish_eaten}int' )

    List_of_teeth = [140, 150, 160, 170, 180, 190, 200, 210, 220]
    n_teeth = random.choice(List_of_teeth)

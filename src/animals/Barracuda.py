from __future__ import annotations
import random

from animals.Fish import Fish 
from foods.Food import Meat

class Barracuda(Fish):
    
    n_fish_eaten: int
    teeth_options = [140, 150, 160, 170, 180, 190, 200, 210, 220]
    # each set of Barraudas that spawn have different sets of teeth 
    n_teeth: int
    luck: bool

    size = 30
    speed = 50
    friendliness = 5
    diet = [Meat]

    def __init__(self: Barracuda, args: dict[str, object]) -> None:
        """
        Create a new Barracuda.
        Pick the random number of teeth for each barracuda that spawn. 
        Set the number of fish eaten to zero.

        Expected args:
            - name
            - gender
        """
        super().__init__(args)

        self.n_fish_eaten = 0
        self.n_teeth = random.choice(self.teeth_options)
        self.luck = random.randint(1, 5)

        self.set_shared_info()

    def swim(self: Barracuda, duration: int) -> None: 
        """
        The specfic size defines what the number of fish can be eaten and then prints the 
        number they have eaten.
        Furthermore, takes in the duration of swim time and mutiples with the appetite to recive new number of fish eaten 
        """
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
        """
        The number of fish eaten impacts the the chance of losing a few sets of teeth, the 
        amount the Barracuda loses ranges mostly around 10
        """
        
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
        lines = super().format_info_lines()
        lines.extend([
            f'Teeth: {self.n_teeth}',
            f'Luck: {self.luck}'
        ])
        return lines

if __name__ == '__main__':
    b = Barracuda('LOL', 'F')
    b.swim(5)   

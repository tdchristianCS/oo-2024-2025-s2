from __future__ import annotations

from animals.Animal import Animal
from animals.Equine import Equine
import random

from foods.Food import Apple

class Horse(Equine): 
    """ 
    A Horse is a type of Equine, which is an animal, which is an Entity that 
    is meant to interact with other entities present in the game through 
    movement and consumption. Their main attack is done through trample. They can 
    only move on land.
    """
    can_lock_legs: bool    
    hunger_pct: int 
    memory_capability: int
    friendliness = 80
    speed = 70
    size = 70
    diet = [Apple]


    def __init__(self: Horse, args: dict[str, object]) -> None:
        """
        Expected args:
          - name 
          - gender
        """
        super().__init__(args)
        
        
        self.set_shared_info()

    def trample(self: Horse, victim: Animal):
        """
        Trample is the horse's attack mode 
        - assign a random int from 1 to 50 
        - depending on the # the attack and success of attack varies 
        - prints the final statement which says who was trampled how efective 
          it was and what the victim is like now
        """
        force = random.randint(1, 50)
        if force < 5: 
            squash = 'poor'
            status = 'no injuries'
        elif force < 15: 
            squash = 'slightly succesfull'
            status= 'a little boo boo'
        elif force < 30: 
            squash = 'succesfull'
            status = 'pain'
        elif force < 45: 
            squash = 'quite succesfull'
            status = 'death'
        else: 
            squash = 'SUCCESS'
            status = 'there was an animal there?'
        print(f'Attack on {victim} was {squash}, they have {status}') 


    def move(self: Horse, duration: int) -> None:
      """Returns how long horse has been moving"""
      self.walk(duration) 
    def walk(self: Horse, duration: int) -> None:
        """Returns nothing"""
        pass 

    def format_info_lines(self: Horse) -> list[str]:
        """Responsble for formating information popup"""
        lines = super().format_info_lines()
        lines.extend([
            f'Fur: {self.fur_colour}'
        ])
        return lines
       



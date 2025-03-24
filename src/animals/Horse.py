from animals.Animal import Animal
from animals.Equine import Equine
from __future__ import annotations
import random

from foods.Food import Apple

class Horse(Equine): 
    can_lock_legs: bool     #true :), so they don't fall while sleeping 
    hunger_pct: int 
    memory_capability: int
    # Assuming that we can measure this on sonme sort of scale where different
    # sides: 0 being Dory Level --> 100 being MEGA MIND MEMORY 
    # (cause horses are big brain??)

    def __init__(self: Horse, args: dict[str, object]) -> None:
        super().__init__(args)

        self.friendliness = 80
        self.speed = 70
        self.size = 110
        self.diet = [Apple]

    def trample(self: Horse, victim: Animal):
        # Thinking about changing this to be impacted by energy. 
        # The amount of energy the horse has the more is it able to attack. 
        # For example, energy is gained through sleep and eating, 
        # if their energy is above x amount, then they can trample 
        # but, if not, they have to run away or get hurt or whatever. 
        # As long as their energy is above x, they can keep trampling 
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
      self.walk(duration) 
    def walk(self: Horse, duration: int) -> None:
        pass
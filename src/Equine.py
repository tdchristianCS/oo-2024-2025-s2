from __future__ import annotations 
from Mammal import Mammal 

class Equine(Mammal): 
# Equines are animals that are a part of the horse family
# such as horses(duh), zebras, ponies, donkeys, mule, etc.

# TODO move different attributes to proper places 

    fur_colour: str 
    teeth_power: int 
    patterns: str  
          # Not sure about keeping the height but considering that equines come in different sizes
                     # maybe keep it but it could also just depend on the type when doing those instead 
    ride: bool  
    sleep_standing: bool  
    # Maybe this too, can we measure frendliness for all animals, probably but are things like sponges friendly?
    # Would their friendliness be the default of 0, not friendly at all?
    can_neigh: bool
    elegance_pct: int
    usablity: int 
    betable: bool 
    tail_length: int
    can_be_made_into_materials: bool 
    stable_worthy: bool 
    horse_power: int 
    herd_animal: bool 


    def __init__(self: Equine, name: str, gender: str, fur_colour: str, teeth_power: int, patterns: str, ride: bool, sleep_standing: bool, can_neigh: bool, betable: bool, can_be_made_into_materials: bool, stable_worthy: bool, herd_animal: bool) -> None:
        super().__init__(name, gender)

        self.fur_colour = fur_colour
        self.teeth_power = teeth_power
        self.patterns = patterns 
        self.ride = ride 
        self.sleep_standing = sleep_standing
        self.can_neigh = can_neigh
        self.betable = betable 
        self.can_be_made_into_materials = can_be_made_into_materials
        self.stable_worthy = stable_worthy 
        self.herd_animal = herd_animal




         









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
    stubborness: int 
    trained: bool 
    elegance_pct: int
    can_be_used_by_humans_for_transportation_of_goods_and_humans_or_other_live_things: bool #??? all of this to be a bool
    betable: bool 
    tail_length: int
    can_be_made_into_materials: bool 
    stable_worthy: bool 
    horse_power: int 
    herd_animal: bool 


    def __init__(self: Equine, name: str, gender: str, fur_colour: str, teeth_power: int, patterns: str, ride: bool, sleep_standing: bool, can_neigh: bool) -> None:
        super().__init__(name, gender)

        self.fur_colour = fur_colour
        self.teeth_power = teeth_power
        # Not going to asign a default for speed, leaving that up to the classes below
        self.patterns = patterns 
        # Same with height
        self.ride = ride 
        self.sleep_standing = sleep_standing
        # Same with IQ and Friendliness
        self.can_neigh = can_neigh

         









from __future__ import annotations 
from Mammal import Mammal 

class Equine(Mammal): 
# Equines are animals that are a part of the horse family
# such as horses(duh), zebras, ponies, donkeys, mule, etc.
    fur_colour: str 
    teeth_power: int 
    speed: int 
    patterns: str  
    height: int      # Not sure about keeping the height but considering that equines come in different sizes
                     # maybe keep it but it could also just depend on the type when doing those instead 
    ride: bool  
    sleep_standing: bool 
    IQ: int          # Follow the equine IQ measurement
    friendliness: int 

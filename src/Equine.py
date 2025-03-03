from __future__ import annotations 

from Mammal import Mammal 
#because a mammal it already has n_legs = 4 
#and all the other characteristics of things above them 

class Equine(Mammal): 
    fur_colour: str 
    teeth_power: int 
    speed: int 
    patterns: str
    height: int
    #not sure about keeping the height but considering that equines come in different sizes
    #maybe keep it but it could also just depend on the type when doing those instead 
    ride: bool  
    sleep_standing: bool 
    IQ: int #follow the equine IQ level

from __future__ import annotations 

from Mammal import Mammal 
#because a mammal it already has n_legs = 4 
#and all the other characteristics of things above them 

class Equine(Mammal): 
    fur_colour: str 
    teeth_power: int 
    speed: int 
    patterns: bool  #for simple purposes the equine either has or doesn't have a pattern 
                    #there is no in between or special patterns :)
    height: int 

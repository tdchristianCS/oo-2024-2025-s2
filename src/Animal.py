from __future__ import annotations

from GameObject import GameObject

class Animal:
    age: int        # This is in seconds
    name: str
    gender: str
    n_legs: int
    height: int
    IQ: int         
    friendliness: int
    speed: int
    sstubborness: int 


    def __init__(self: Animal, name: str, gender: str) -> None:
        # First we create the attributes that came from arguments
        self.name = name
        self.gender = gender

        # Then we set the attributes that have default values
        self.age = 0

        # For n_legs, there may be no default value that makes sense
        # It is OK for this to have no value; it will cause an error
        # if someone tries to access it, which is OK.

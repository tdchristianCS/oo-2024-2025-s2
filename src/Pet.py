"""
Pet
-	hitbox_diameter: int
-	weight: int
-	diet_type: str
-	foods: list[str]
-	n_legs: int
-	species: str
-	skin_type: str
-	has_tail: bool
-	can_play: bool
-	daily_walk_req: int
-	can_swim: bool
-	cleanliness_level: int
-	happiness_level: int
-	hunger_level: int
-	energy_level: int
-	wash() -> int
-	pet() -> int
-	feed(str) -> int
-	walk() -> list[int, int] # reduces weight and energy level
-	do_business()
-	watch_intruder()
"""

class Pet:
    name: str
    age: int
    weight: int
    species: str
    cleanliness: int
    happiness: int
    energy: int
    hunger: int

    def __init__(self, name: str, species: str, weight: int) -> None:
        self.name = name
        self.species = species
        self.weight = weight

        self.age = 0
        self.cleanliness = 100
        self.happiness = 100
        self.energy = 100
        self.hunger = 100

pets = [
    Pet('Rover', 'dog', 5),
    Pet('Sassy', 'cat', 1)
]

from Cat import Cat
from Otter import Otter
from Dog import *

cats = [
    Cat('Yannis', 'M', 'BLACK'),
    Cat('Edwin', 'M', 'ORANGE'),
    Cat('Jonathan', 'M', 'NEON'),
    Cat('Daniel', 'M', 'GREEN'),
    Cat('Giovanni', 'M', 'BROWN'),
    Cat('Michael', 'M', 'RED'),
    Cat('Julia', 'F', 'PURPLEYELLOW'),
    Cat('Dylan', 'M', 'TUXEDO'),
    Cat('Kyle', 'M', 'INVISIBLE')
]

otters = [
    Otter('John Doe', 'M'),
    Otter('Jane Doe', 'F'),
    Otter('Baab', 'M'),
    Otter('Bobette', 'F'),
    Otter('Julius Caesar', 'M'),
    Otter('Julia Caesar', 'F'),
]

dogs = [
    Husky('Ethan Thomas', 'M'),
    Chihauhua('Josh Payne', 'M'),
    Mutt('Owen Dryer', 'M'),
    Mutt('Joel Nosenan', 'M'),
    Mutt('Daniel', 'M'),
    Mutt('Joel', 'M'),
]

animals = cats + otters + dogs

for animal in animals:
    animal.move(5)

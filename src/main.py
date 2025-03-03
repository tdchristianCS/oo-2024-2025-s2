from Cat import Cat
from Otter import Otter

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

animals = cats + otters

for animal in animals:
    animal.move(5)
    animal.move(5)

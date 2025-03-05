from Cat import Cat
from Otter import Otter
from Capybara import Capybara
from Dog import *

Capybaras = [
    Capybara("John Capybara", "M", "brown", 125, ["grass"]),
    Capybara("Jane Capybara", "F", "brown", 120, ["grass"])
]
for i in Capybaras:
    i.swim(999999)

# cats = [
#     Cat('Yannis', 'M', 'BLACK'),
#     Cat('Edwin', 'M', 'ORANGE'),
#     Cat('Jonathan', 'M', 'NEON'),
#     Cat('Daniel', 'M', 'GREEN'),
#     Cat('Giovanni', 'M', 'BROWN'),
#     Cat('Michael', 'M', 'RED'),
#     Cat('Julia', 'F', 'PURPLEYELLOW'),
#     Cat('Dylan', 'M', 'TUXEDO'),
#     Cat('Kyle', 'M', 'INVISIBLE')
# ]
dogs = [
    Husky('Ethan Thomas', 'M'),
    Chihauhua('Josh Payne', 'M'),
    Mutt('Owen Dryer', 'M'),
    Mutt('Joel Nosenan', 'M'),
    Mutt('Daniel', 'M'),
    Mutt('Joel', 'M')
]


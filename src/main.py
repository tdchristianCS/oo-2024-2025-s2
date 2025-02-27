from animals.Cat import Cat

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

for cat in cats:
    cat.walk()

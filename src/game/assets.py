import pygame.image

# TODO automate animal naming

keys = [
    'capybara', 'horse', 'elephant', 'cat', 'shark', 'mutt', 'husky', 'chihuahua', 'wolf', 'barracuda', 'otter', 'rat'
]

assets = {}
for key in keys:
    assets[key] = pygame.image.load(f'src/assets/{key}.png')

tr_60 = pygame.image.load('src/assets/60.png')

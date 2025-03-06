import pygame.image

# TODO automate animal naming

keys = [
    'capybara', 'horse', 'elephant', 'cat', 'shark', 'mutt', 'husky', 'chihuahua', 'wolf',
    # fish
]

assets = {}
for key in keys:
    assets[key] = pygame.image.load(f'src/assets/{key}.png')

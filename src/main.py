MSG = """
pygame demo f: movement, continuous
Shows moving an object when an event fires,
and continuing to move until another event fires.
Use WASD or the arrow keys to test it out. You do not have to hold them.
Watch the console for info about the object's X and Y positions.
"""

print(MSG)

import pygame

# Create a GameState object to store global variables
from game.Game import Game, GameState
from game.GameObject import GameObject

from animals.Cat import Cat
from animals.Capybara import Capybara
from animals.Horse import Horse

# Make game object
game = Game(1680, 900)

# Set up the window
pygame.init()
pygame.display.set_caption('Noah\'s Ark')
window = pygame.display.set_mode([game.width, game.height])

# Initialize game variables
gsRunning = GameState('running')
gsQuit = GameState('quit')

# Animals
# Dummy code...
# game.objects.extend([
#     GameObject(Cat('Dinky', 'M', 'brown'), (100, 100)),
#     GameObject(Cat('Army', 'F', 'black'), (200, 200)),
#     GameObject(Capybara('Pinky', 'M', 'pink'), (400, 400)),
#     GameObject(Horse('Stinky', 'F', 'white'), (300, 300)),
# ])
game.spawn_animals()

# Images
img_bg = pygame.image.load('src/assets/bg.png')
img_bg = pygame.transform.scale(img_bg, (game.width, game.height))

# Functions

def draw_bg(surface) -> None:
    surface.blit(img_bg, (0, 0))

game.state = gsRunning

while game.state == gsRunning:
    # Check events
    for event in pygame.event.get():

        # User clicks window close button
        if event.type == pygame.QUIT:
            game.state = gsQuit
    
    # Draw
    draw_bg(window)
    for o in game.objects:
        o.draw(window)
        o.draw_hitbox(window)

    # Update the display
    pygame.display.flip()

# Quit the window
pygame.quit()

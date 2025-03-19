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
from game.Level import Level

from animals.Cat import Cat
from animals.Capybara import Capybara
from animals.Horse import Horse

# Make game object
game = Game(1680, 900)
# game = Game(1400, 800)

# Set up the window
pygame.init()
pygame.display.set_caption('Noah\'s Ark')
window = pygame.display.set_mode([game.width, game.height])

# Font
pygame.font.init()
font_debug = pygame.font.SysFont('Courier New', 24)

# Clipboard
pygame.scrap.init()

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
level = Level('zoolandia', img_bg)
game.set_level(level)

# Functions

game.state = gsRunning

while game.state == gsRunning:

    # Check events
    for event in pygame.event.get():

        # User clicks window close button
        if event.type == pygame.QUIT:
            game.state = gsQuit

        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            debug_text = font_debug.render(str(pos), False, (255, 255, 255))

# TODO
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()

        #     # Left
        #     if pygame.mouse.get_pressed()[0]:
        #         pygame.scrap.put(pygame.SCRAP_TEXT, 'chung'.encode())
                # pygame.scrap.put(pygame.SCRAP_TEXT, str(pos).encode())
            
    
    # Draw
    game.level.draw(window)
    game.level.draw_water(window) # Debugging

    for o in game.objects:
        o.draw(window)
        o.draw_hitbox(window) # Debugging

    window.blit(debug_text, (game.width // 2, game.height - 40)) # Debugging

    # Update the display
    pygame.display.flip()

# Quit the window
pygame.quit()

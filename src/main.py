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

W = 1680
H = 900

# Set up the window
pygame.init()
pygame.display.set_caption('Noah\'s Ark')
window = pygame.display.set_mode([W, H])

# Initialize game variables
game = Game()
gsRunning = GameState('running')
gsQuit = GameState('quit')

# Images
img_bg = pygame.image.load('src/assets/bg.png')
img_bg = pygame.transform.scale(img_bg, (W, H))

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
    
    draw_bg(window)

    # Update the display
    pygame.display.flip()

# Quit the window
pygame.quit()

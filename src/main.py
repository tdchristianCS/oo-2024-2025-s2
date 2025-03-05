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
from game import tools
gs = tools.GameState()

# Set up the window
pygame.init()
pygame.display.set_caption('My very first pygame GUI')
window = pygame.display.set_mode([400, 400])

# Initialize game variables
gs.player_x = 200
gs.player_y = 200
gs.direction = ''

# Set up FPS
gs.set_fps(30)

# Functions

def change_direction(event) -> None:
    """
    Change the player's movement direction using
    WASD or arrow keys.
    """

    if event.key in [pygame.K_w, pygame.K_UP]:
        gs.direction = 'N'

    elif event.key in [pygame.K_s, pygame.K_DOWN]:
        gs.direction = 'S'

    elif event.key in [pygame.K_a, pygame.K_LEFT]:
        gs.direction = 'W'

    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
        gs.direction = 'E'

    print(f'Player direction changed to {gs.direction}')

def move() -> None:
    """
    Move the player according to the direction it's facing.
    """

    if gs.direction == 'N':
        if gs.player_y > 25:
            gs.player_y -= 10

    elif gs.direction == 'S':
        if gs.player_y < 375:
            gs.player_y += 10

    elif gs.direction == 'W':
        if gs.player_x > 25:
            gs.player_x -= 10

    elif gs.direction == 'E':
        if gs.player_x < 375:
            gs.player_x += 10

    print(f'Player moved to ({gs.player_x}, {gs.player_y})')

# Main loop
running = True
while running:

    # Catch all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            change_direction(event)
    
    # Move
    move()
    
    # Draw the background
    pygame.draw.rect(window, 'black', (0, 0, 400, 400))

    # Draw the player
    pygame.draw.circle(window, 'white', (gs.player_x, gs.player_y), 20)

    # Update the display
    pygame.display.flip()

    # Wait for next frame
    gs.wait_fps()

# Quit the window
pygame.quit()

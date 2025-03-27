import pygame

# Create a GameState object to store global variables
from game.Game import Game, GameState
from game.Level import Level

# Make game object
game = Game(1440, 800)

# Set up the window
pygame.init()
pygame.display.set_caption('Noah\'s Ark')
window = pygame.display.set_mode([game.width, game.height])

# Font
pygame.font.init()
font_debug = pygame.font.SysFont('Courier New', 24)
font_info = pygame.font.SysFont('Comic Sans', 16)

# Initialize game variables
gs_running = GameState('running')
gs_running.set_fps(60)

gs_quit = GameState('quit')

# Level
img_bg = pygame.image.load('src/assets/bg.png')
img_bg = pygame.transform.scale(img_bg, (game.width, game.height))
level = Level('zoolandia', img_bg)
game.set_level(level)

# Animals
game.spawn_animals()

# Timed events
e_spawn_animal = pygame.USEREVENT + 1
pygame.time.set_timer(e_spawn_animal, 1_000)

# Debugging...
# game.debug_mousedown_pos = None
# game.debug_mouseup_pos = None
# game.debug_pos_pairs = []
# game.debug_rect = None
# game.debug_rects = []

# def get_debug_rectangle() -> None:
#     left, top = game.debug_mousedown_pos
#     right, bottom = pygame.mouse.get_pos()
#     return pygame.Rect(left, top, right - left, bottom - top)

# Main loop
game.state = gs_running
while game.state == gs_running:

    # debug_text = None

    # Check events
    for event in pygame.event.get():

        # User clicks window close button
        if event.type == pygame.QUIT:
            game.state = gs_quit

        # Spawn animal
        elif event.type == e_spawn_animal:
            game.spawn_animal()

        # elif event.type == pygame.MOUSEMOTION:
        #     pos = pygame.mouse.get_pos()
        #     debug_text = font_debug.render(str(pos), False, (255, 255, 255))

        #     if game.debug_mousedown_pos:
        #         game.debug_rect = get_debug_rectangle()

        # # Debugging drawing rectangles
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     game.debug_mousedown_pos = pygame.mouse.get_pos()
        
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     game.debug_mouseup_pos = pygame.mouse.get_pos()
        #     game.debug_rects.append(game.debug_rect)
        #     game.debug_pos_pairs.append([game.debug_mousedown_pos, game.debug_mouseup_pos])

        #     with open('src/debug/rects.txt', 'w') as f:
        #         for pair in game.debug_pos_pairs:
        #             tl, br = pair
        #             f.write(f'water::{tl[0]},{tl[1]}::{br[0]},{br[1]}\n')

        #     game.debug_mousedown_pos = None
        #     game.debug_rect = None            
    
    # Draw
    game.level.draw(window)
    # game.level.draw_water(window) # Debugging

    mp = pygame.mouse.get_pos()
    for o in game.objects:
        o.update()
        o.draw(window)
        # o.draw_hitbox(window) # Debugging
        # o.draw_info(window, font_info)

    for o in game.objects:
        if o.rect.collidepoint(mp):
            o.draw_info(window, font_info)
            break

    # # Debug
    # if debug_text:
    #     window.blit(debug_text, (game.width // 2, game.height - 40)) # Debugging
    # if game.debug_rect:
    #     pygame.draw.rect(window, '#0055ff', game.debug_rect)
    # for rect in game.debug_rects:
    #     pygame.draw.rect(window, '#0022ff', rect)

    # Update the display
    pygame.display.flip()

    game.state.wait_fps()
    game.state.fps_clock.tick()

# Quit the window
pygame.quit()

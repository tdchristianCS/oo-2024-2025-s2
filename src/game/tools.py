from __future__ import annotations
from enum import Enum
import pygame

# Considering using a GameState as a global variable to hold all settings.

# Usage example:
# from library.tools import GameState
# game = GameState()
# game.move_speed = 50

class GameState:
    """
    Represents the state of a game for the purpose of storing variables
    and accessing them throughout a program. Also provides some functions
    to make life easier.
    """
    fps: int
    fps_delay: int
    fps_clock: pygame.time.Clock

    # def __init__(self: GameState) -> None:
    #     self.set_fps(30)
    
    # Frames per second solution.
    # At the start of your code, once you have a GameState,
    # call set_fps on it with and desired FPS value.
    # At the end of your main loop, call wait_fps on your GameState.
    # Note that GameState has a default FPS value of 30.

    def set_fps(self: GameState, fps: int) -> None:
        """
        Set this GameState to run at the given frames per second.
        Typical values: 15, 30, 60, 90, 120, 240.

        Also set the keyboard to allow holding down keys (this means that
        a new 'keydown' event is sent once per frame).
        """
        self.fps = fps
        self.fps_delay = 1_000 // self.fps
        self.fps_clock = pygame.time.Clock()
        pygame.key.set_repeat(self.fps_delay)

    def wait_fps(self: GameState) -> None:
        """
        Cause the game to wait the appropriate amount of time to ensure a smooth FPS.
        """
        self.fps_clock.tick(self.fps)

class Button:
    """Represents a button. Specify the coordinates when creating or blitting it.
    These coordinates are the top left of the button's visible representation.
    Set its surface (e.g. a shape), text, or image. Use check_hover
    and check_click to respond to user actions.
    """
    coords: tuple[int]
    surface: pygame.display.Surface
    w: int
    h: int
    enabled: bool

    def __init__(self: Button, coords: tuple[int]=None) -> None:
        """Create a button. If you specify (x, y) coordinates (top left corner)
        as a list of two numbers, these will be saved and used when displaying it.
        However, you can also defer specifying these until blitting,
        in which case their temporary values will be (0, 0)."""
        if not coords:
            coords = (0, 0)

        self.set_coords(coords)
        self.set_text(self.get_default_text())
        self.enable()

    def disable(self: Button) -> None:
        self.enabled = False
    
    def enable(self: Button) -> None:
        self.enabled = True

    def get_default_text(self: Button) -> pygame.display.Surface:
        """Create a default text box."""
        pygame.font.init()
        font = pygame.font.SysFont('Courier New', 24)
        return font.render('[Default button text]', True, 'black', 'white')
    
    def set_surface(self: Button, surface: pygame.display.Surface) -> None:
        """Set the button's visible representation to the given pygame Surface."""
        self.surface = surface
        self.w = self.surface.get_width()
        self.h = self.surface.get_height()

    def set_text(self: Button, text: pygame.display.Surface) -> None:
        """Set the button's visible representation to the given text."""
        self.set_surface(text)
    
    def set_image(self: Button, img: pygame.display.Surface) -> None:
        """Set the button's visible representation to the given image."""
        self.set_surface(img)

    def set_coords(self: Button, coords: tuple[int]) -> None:
        """Set the button's coordinates to the given pair of numbers."""
        self.coords = coords

    def get_bounds(self: Button) -> tuple[int]:
        """Return the button's bounds as specified by the top (left) x and y
        and the bottom (right) x and y values, all as one list."""
        tx, ty = self.coords
        bx, by = tx + self.w, ty + self.h
        return (tx, ty, bx, by)
    
    def check_hover(self: Button) -> bool:
        """Return True iff the player's cursor is over this button."""
        if not self.enabled:
            return False
        
        ox, oy, dx, dy = self.get_bounds()
        mx, my = pygame.mouse.get_pos()
        return (ox < mx < dx) and (oy < my < dy)
    
    def check_click(self: Button, mb: int=0) -> bool:
        """
        Return True iff the player's cursor is on this button and they're clicking.
        mb is an int for which mouse button to check. Default 0 = left.
        Optionally specify 1 = middle or 2 = right. 
        """
        if not self.enabled:
            return False
        
        return pygame.mouse.get_pressed()[mb] and self.check_hover()
    
    def blit(self: Button, window: pygame.display.Surface, new_coords: tuple[int]=None) -> None:
        """
        Display this button on the given surface. Uses the saved (x, y) coordinates
        by default, but optionally provide new coordinates as a list of two numbers.
        """
        if new_coords:
            self.set_coords(new_coords)
            
        window.blit(self.surface, self.coords)

class Direction(Enum):
    N: str = 'N'
    E: str = 'E'
    S: str = 'S'
    W: str = 'W'
    NW: str = 'NW'
    NE: str = 'NE'
    SW: str = 'SW'
    SE: str = 'SE'
    NONE: str =''

def get_cardinal_movement(event) -> str:
    """
    Return a cardinal direction ('N', 'E', 'S', 'W' or '' for no movement),
    based on the keys being pressed in the given event object.
    Recognizes arrow keys and WASD.
    """
    if event.key in [pygame.K_w, pygame.K_UP]:
        return Direction.N
    elif event.key in [pygame.K_s, pygame.K_DOWN]:
        return Direction.S
    elif event.key in [pygame.K_a, pygame.K_LEFT]:
        return Direction.E
    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
        return Direction.W
    else:
        return Direction.NONE

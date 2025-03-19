from __future__ import annotations
import pygame
import random

from game.GameObject import GameObject
from game.Point import Point
from animals.Animal import Animal
from animals.Capybara import Capybara
from animals.Cat import Cat
from animals.Dog import Dog
from animals.Elephant import Elephant
from animals.Horse import Horse
from animals.Otter import Otter
from animals.Rat import Rat
from animals.Shark import Shark

MIN_ANIMALS = 2
MAX_ANIMALS = 20
ANIMALS = [Capybara, Cat, Dog, Elephant, Horse, Otter, Rat, Shark]

class Game:
    objects: GameObject
    state: GameState

    def __init__(self: Game) -> None:
        self.state = None
        self.objects = []

    def spawn_animals(self: Game) -> None:
        n_animals = random.randint(MIN_ANIMALS, MAX_ANIMALS)
        for _ in range(n_animals):
            animal = self.spawn_animal()
            self.objects.append(animal)

    def spawn_animal(self: Game) -> GameObject:
        animal = self.choose_animal()
        point = self.choose_point()
        return GameObject(animal, point)
    
    def choose_animal(self: Game) -> Animal:
        animal_class = random.choice(ANIMALS)
        return animal_class.make_random()
    
    def choose_point(self: Game) -> Point:
        return None

class GameState:
    """
    Represents the state of a game for the purpose of storing variables
    and accessing them throughout a program. Also provides some functions
    to make life easier.
    """
    name: str
    fps: int
    fps_delay: int
    fps_clock: pygame.time.Clock

    def __init__(self: GameState, name: str) -> None:
        self.name = name
    
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

    def __eq__(self: GameState, other: object) -> bool:
        return (type(other) == type(self)) and (self.name == other.name)

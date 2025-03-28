from __future__ import annotations
import pygame
import random

from game.GameObject import GameObject
from game.Entity import Entity
from game.Point import Point
from game.Level import Level

from animals.Animal import Animal
from animals.Capybara import Capybara
from animals.Cat import Cat
from animals.Dog import Husky, Chihuahua, Mutt
from animals.Elephant import Elephant
from animals.Horse import Horse
from animals.Otter import Otter
from animals.Rat import Rat
from animals.Shark import Shark
from animals.Barracuda import Barracuda

from game.constants import TERRAIN_LAND, TERRAIN_WATER

MIN_ANIMALS = 1
MAX_ANIMALS = 10
ANIMALS = [Capybara, Cat, Husky, Chihuahua, Mutt, Elephant, Horse, Otter, Rat, Shark, Barracuda]
# ANIMALS = [Cat]

class Game:
    objects: GameObject
    state: GameState
    width: int
    height: int
    level: Level

    def __init__(self: Game, width: int, height: int) -> None:
        self.state = None
        self.objects = []
        self.width, self.height = width, height
        self.level = None

    def set_level(self: Game, level: Level) -> None:
        self.level = level

    def spawn_animals(self: Game) -> None:
        n_animals = random.randint(MIN_ANIMALS, MAX_ANIMALS)
        for _ in range(n_animals):
            animal = self.create_animal()
            if animal:
                self.objects.append(animal)

    def spawn_animal(self: Game) -> None:
        animal = self.create_animal()
        if animal:
            self.objects.append(animal)

    def create_animal(self: Game) -> GameObject:
        animal = self.choose_animal()
        point = self.choose_point(animal)
        if point:
            return GameObject(animal, point)
    
    def choose_animal(self: Game) -> Animal:
        animal_class = random.choice(ANIMALS)
        return Animal.make_random_animal(animal_class)
    
    def choose_point(self: Game, entity: Entity) -> Point:
        w = entity.image.get_width()
        h = entity.image.get_height()
        min_x = round(w / 2)
        min_y = round(h / 2)
        max_x = self.width - min_x
        max_y = self.height - min_y

        # Water: keep trying until valid point is found

        x = random.randint(min_x, max_x)
        y = random.randint(min_y, max_y)
        rect = pygame.Rect(x - (w / 2), y - (w / 2), w, h)
        while not self.can_spawn_here(entity, rect):
            x = random.randint(min_x, max_x)
            y = random.randint(min_y, max_y)
            rect = pygame.Rect(x - (w / 2), y - (w / 2), w, h)

        # Other animal: give up if on top of
        if not self.is_on_object(rect):
            return Point(x, y)

    def can_spawn_here(self: Game, entity: Entity, check_rect: pygame.Rect) -> bool:
        options = [
            TERRAIN_LAND in entity.terrains and self.is_on_land(check_rect),
            TERRAIN_WATER in entity.terrains and self.is_on_water(check_rect)
        ]

        return any(options)
    
    def is_on_land(self: Game, check_rect: pygame.Rect) -> bool:
        for water_rect in self.level.water_rects:
            if check_rect.colliderect(water_rect):
                return False
        return True
    
    def is_on_water(self: Game, check_rect: pygame.Rect) -> bool:
        corners = {
            check_rect.topleft: False,
            check_rect.topright: False,
            check_rect.bottomleft: False,
            check_rect.bottomright: False
        }
        for water_rect in self.level.water_rects:
            for corner in corners:
                if water_rect.collidepoint(corner):
                    corners[corner] = True
            
            if all(corners.values()):
                return True
            
        return False
    
    def is_on_object(self: Game, check_rect: pygame.Rect) -> bool:
        for object in self.objects:
            if check_rect.colliderect(object.rect):
                return True
        return False
    
    def update_objects(self: Game) -> None:
        new_objects = []
        for o in self.objects:
            still_alive = o.update()
            if still_alive:
                new_objects.append(o)
        self.objects = new_objects

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

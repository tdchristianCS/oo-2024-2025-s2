from __future__ import annotations

from animals.Animal import Animal

# Interface
# Defines operations but has no concrete realization
# There is no animal called a "movable"; instead,
# it's just there to provide a move template to all
# animals that can move.

class Movable(Animal):

    # Because there is no concrete object called a "movable",
    # it makes no sense to have a concrete body for our move function
    # When we raise NotImplementedError, this FORCES all lower classes
    # to implement the method.
    def move(self: Movable) -> None:
        raise NotImplementedError
    
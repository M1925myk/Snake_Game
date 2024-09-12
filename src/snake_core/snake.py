from dataclasses import dataclass
from enum import Enum

from .shapes import SquareShape
from .utils import Position


class Direction(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'


class Snake:
    def __init__(self, initial_length=1):
        self._length = initial_length
        self.body = Position * initial_length
        self.direction = Direction.RIGHT

    def move(self, direction: Direction) -> None:
        delta_x = delta_y = 0
        match direction:
            case Direction.UP:
                delta_y = -1
            case Direction.DOWN:
                delta_y = 1
            case Direction.LEFT:
                delta_x = -1
            case Direction.RIGHT:
                delta_x = 1

        new_head = SnakeBodyPart(
            shape=SquareShape(
                center=Position(
                    x=self._body[0].shape.center.x + delta_x,
                    y=self._body[0].shape.center.y + delta_y,
                ),
                edge=10,
            )
        )
        self._body = [new_head] + (self._body if self._ready_to_grow else self._body[:-1])
        self._ready_to_grow = False


    def grow(self) -> None:
        self._ready_to_grow = True

    @property
    def size(self) -> int:
        return len(self._body)


@dataclass
class SnakeBodyPart:
    shape: SquareShape

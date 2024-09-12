from .utils import Position


class Shape:
    pass


class SquareShape(Shape):
    def __init__(self, center: Position, edge: int) -> None:
        self.center = center
        self.edge = edge

    def is_collided(self, another_shape: 'SquareShape') -> bool:
        raise NotImplemented

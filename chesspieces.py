from abc import ABC
from dataclasses import dataclass
from enum import StrEnum, auto


class Chesscolor(StrEnum):
    BLACK = auto()
    WHITE = auto()


@dataclass
class Chesspiece(ABC):
    color: Chesscolor
    _moved: bool = False

    def possible_moves_from_position(self, row: int, column: int) -> [[]]:
        raise NotImplementedError


class King(Chesspiece):
    pass


class Queen(Chesspiece):
    pass


class Rook(Chesspiece):
    pass


class Bishop(Chesspiece):
    pass


class Pawn(Chesspiece):
    pass


class Knight(Chesspiece):
    pass

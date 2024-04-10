from abc import ABC, abstractmethod
from typing import List

from back.models.errors import IllegalMoveError


class Piece(ABC):
    LABEL = None

    @abstractmethod
    def __init__(self):
        self.row = None
        self.col = None
        self.player = None
        self.allowed_positions = []

    @property
    def possible_positions(self):
        # corresponds to natural piece movement if nothing interferes
        pass

    @property
    def possible_capture_positions(self):
        # corresponds to positions that are only reachable when capturing other pieces
        pass

    @abstractmethod
    def update_allowed_positions(self, chess_model):
        """
        :param board: current board
        :param row: row of the piece in the board
        :param col: col of the piece in the board
        :return:
        modifies self.allowed_positions
        """
        pass

    def update_position(self, row, col) -> None:
        if (row, col) in self.allowed_positions:
            self.row = row
            self.col = col
        else:
            raise IllegalMoveError('You might have not updated the position of this piece, '
                                   'or you have made a mistake in possible move implementation')

    def __repr__(self):
        return self.LABEL.value

    def __str__(self):
        return self.LABEL.value

    def __format__(self, format_spec):
        return self.LABEL.value

    def __hash__(self):
        return hash(id(self))

    def __eq__(self, other):
        return hash(id(self)) == hash(id(other))

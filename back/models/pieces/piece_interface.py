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
        self.possible_positions = []

    @abstractmethod
    def update_possible_positions(self, board, row, col) -> List[tuple]:
        """
        :param board: current board
        :param row: row of the piece in the board
        :param col: col of the piece in the board
        :return:
        list of possible rows and cols that are inside the board and that are legal
        """
        pass

    def update_position(self, row, col) -> None:
        if (row, col) in self.possible_positions:
            self.row = row
            self.col = col
        else:
            raise IllegalMoveError('You might have not updated the position of this piece')

    def __repr__(self):
        return self.LABEL.value

    def __str__(self):
        return self.LABEL.value

    def __format__(self, format_spec):
        return self.LABEL.value


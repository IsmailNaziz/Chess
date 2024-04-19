from typing import Callable

from back.configuration import BOARD_SIZE
from back.models.pieces.piece_interface import Piece
from back.models.pieces.piece_labels import PIECE_LABEL
from back.models.player.player import PLAYER
from back.tool_box import is_in_bound


class Bishop(Piece):
    LABEL = PIECE_LABEL.BISHOP

    def __init__(self, row: int, col: int, player: PLAYER):
        self.row = row
        self.col = col
        self.player = player
        self.allowed_positions = []

    @property
    def possible_positions(self):
        # corresponds to natural piece movement if nothing interferes
        return [(possible_row, possible_col)
                for possible_row in range(BOARD_SIZE) for possible_col in range(BOARD_SIZE)
                if (self.row + self.col == possible_row + possible_col) or
                (self.row - self.col == possible_row - possible_col)]

    def update_allowed_positions(self, chess_model):
        """
        :param chess_model: current chess_model
        :param row: row of the piece in the board
        :param col: col of the piece in the board
        modifies self.allowed_positions
        """
        if chess_model.player_turn != self.player:
            self.allowed_positions = []
            return

        in_bound_positions = [position for position in self.possible_positions if is_in_bound(*position)]

        in_sight_line = in_bound_positions
        for piece in chess_model.pieces:
            if (piece.row, piece.col) in in_sight_line:
                filter_function = self.get_dial_filter_function(piece.row, piece.col)
                in_sight_line = [position for position in in_sight_line if filter_function(*position)]
                # possible to capture, manage when values are equal
                if piece.player != self.player:
                    in_sight_line.append((piece.row, piece.col))

        self.allowed_positions = in_sight_line

    def get_dial_filter_function(self, row, col) -> Callable:
        """
                         |
                    1    |    2
                         |
                ---------B---------
                         |
                     3   |    4
                         |
        returns the dial id from given coordinates
        """

        if row <= self.row and col <= self.col:
            return lambda r, c: r < row and c < col

        if row <= self.row and col >= self.col:
            return lambda r, c: r < row and c > col

        if row >= self.row and col <= self.col:
            return lambda r, c: r > row and c < col

        if row >= self.row and col >= self.col:
            return lambda r, c: r > row and c > col


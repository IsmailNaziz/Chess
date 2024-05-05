from typing import List

from back.configuration import BOARD_SIZE
from back.models.pieces.piece_interface import Piece
from back.models.pieces.piece_labels import PIECE_LABEL
from back.models.player.player import PLAYER
from back.tool_box import is_in_bound


class Queen(Piece):
    LABEL = PIECE_LABEL.QUEEN

    def __init__(self, row: int, col: int, player: PLAYER):
        self.row = row
        self.col = col
        self.player = player
        self.allowed_positions = []

    @property
    def possible_positions(self):
        """
        rook + bishop
        """
        # corresponds to natural piece movement if nothing interferes
        diagonal_possible_moves = [(possible_row, possible_col)
                                   for possible_row in range(BOARD_SIZE) for possible_col in range(BOARD_SIZE)
                                   if ((self.row + self.col == possible_row + possible_col) or
                                       (self.row - self.col == possible_row - possible_col))
                                   and (self.row, self.col) != (possible_row, possible_col)]
        straight_line_possible_moves = [(possible_row, self.col) for possible_row in range(BOARD_SIZE)
                                        if possible_row != self.row] + \
                                       [(self.row, possible_col) for possible_col in range(BOARD_SIZE)
                                        if possible_col != self.col]
        return diagonal_possible_moves + straight_line_possible_moves

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

        in_sight_positions = in_bound_positions
        for piece in chess_model.pieces:
            if piece != self and (piece.row, piece.col) in in_sight_positions:
                diagonal_filter_function = self.get_dial_filter_function(piece.row, piece.col)
                straight_line_filter_function = self.get_straight_line_filter_function(piece.row, piece.col)
                in_sight_positions = [position for position in in_sight_positions
                                      if diagonal_filter_function(*position)
                                      and straight_line_filter_function(*position)]
                if piece.player != self.player:
                    in_sight_positions.append((piece.row, piece.col))

        self.allowed_positions = in_sight_positions

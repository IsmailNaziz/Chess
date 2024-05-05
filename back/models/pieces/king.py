from itertools import product
from typing import List

from back.configuration import BOARD_SIZE
from back.models.pieces.piece_interface import Piece
from back.models.pieces.piece_labels import PIECE_LABEL
from back.models.player.player import PLAYER
from back.tool_box import is_in_bound


class King(Piece):
    LABEL = PIECE_LABEL.KING

    def __init__(self, row: int, col: int, player: PLAYER):
        self.row = row
        self.col = col
        self.player = player
        self.allowed_positions = []

    @property
    def possible_positions(self):
        return [(self.row + row_offset, self.col + col_offset)
                for row_offset, col_offset in product([-1, 0, 1], [-1, 0, 1])
                if row_offset != 0 and col_offset != 0]


    def update_allowed_positions(self, chess_model):
        """
        :param chess_model: current chess_model
        :param row: row of the piece in the board
        :param col: col of the piece in the board
        modifies self.allowed_positions
        """
        #TODO: Add castle move

        if chess_model.player_turn != self.player:
            self.allowed_positions = []
            return

        in_bound_positions = [position for position in self.possible_positions if is_in_bound(*position)]
        not_taken_by_aly_piece_positions = [position for position in in_bound_positions
                                            if chess_model.get_position_content_from_indexes(*position) is None]
        self.allowed_positions = not_taken_by_aly_piece_positions

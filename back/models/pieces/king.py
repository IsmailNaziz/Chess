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
        # corresponds to natural piece movement if nothing interferes
        return []

    @property
    def possible_capture_positions(self):
        # corresponds to positions that are only reachable when capturing other pieces
        return []

    def update_allowed_positions(self, chess_model):
        """
        :param chess_model: current chess_model
        :param row: row of the piece in the board
        :param col: col of the piece in the board
        modifies self.allowed_positions
        """

        self.allowed_positions = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)]


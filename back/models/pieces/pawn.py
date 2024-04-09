from typing import List

from back.configuration import BOARD_SIZE
from back.models.pieces.piece_interface import Piece
from back.models.pieces.piece_labels import PIECE_LABEL
from back.models.player.player import PLAYER


class Pawn(Piece):
    LABEL = PIECE_LABEL.PAWN

    def __init__(self, row: int, col: int, player: PLAYER):
        self.row = row
        self.col = col
        self.player = player
        self.allowed_positions = []

    def update_allowed_positions(self, board):
        """
        :param board: current board
        :param row: row of the piece in the board
        :param col: col of the piece in the board
        modifies self.allowed_positions
        """
        #TODO: to be changed, test value only
        self.allowed_positions = [(row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE)]


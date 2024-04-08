from typing import List

from back.models.pieces.piece_interface import Piece
from back.models.pieces.piece_labels import PIECE_LABEL
from back.models.player.player import PLAYER


class Pawn(Piece):
    LABEL = PIECE_LABEL.PAWN

    def __init__(self, row: int, col: int, player: PLAYER):
        self.row = row
        self.col = col
        self.player = player
        self.possible_positions = []

    def update_possible_positions(self, board, row: int, col: int) -> List[tuple]:
        """
        :param board: current board
        :param row: row of the piece in the board
        :param col: col of the piece in the board
        :return:
        list of possible rows and cols that are inside the board and that are legal
        """
        pass

    def __repr__(self):
        print(self.LABEL)


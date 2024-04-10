from typing import List

from back.configuration import BOARD_SIZE
from back.models.pieces.piece_interface import Piece
from back.models.pieces.piece_labels import PIECE_LABEL
from back.models.player.player import PLAYER
from back.tool_box import is_in_bound


class Pawn(Piece):
    LABEL = PIECE_LABEL.PAWN

    def __init__(self, row: int, col: int, player: PLAYER):
        self.row = row
        self.col = col
        self.player = player
        self.allowed_positions = []

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

        translation = 0
        if self.player == PLAYER.PLAYER_1:
            translation = 1
        elif self.player == PLAYER.PLAYER_2:
            translation = -1

        possible_positions = [(self.row+translation, self.col)]  # corresponds to natural piece movement if nothing interferes

        # consecutive filter with explicit variable names
        in_bound_positions = [position for position in possible_positions if is_in_bound(*position)]
        not_taken_by_aly_piece_positions = [position for position in in_bound_positions
                                            if chess_model.get_cell_content_from_indexes(*position) is None]

        # TODO: if the move after been made, makes own player in check position
        possible_capture_positions = [(self.row+translation, self.col+1),
                                      (self.row+translation, self.col-1)]
        valid_capture_positions = []
        for capture_position in possible_capture_positions:
            cell_content = chess_model.get_cell_content_from_indexes(*capture_position)
            if cell_content is not None and cell_content.player != self.player:
                valid_capture_positions.append(capture_position)

        self.allowed_positions = valid_capture_positions + not_taken_by_aly_piece_positions


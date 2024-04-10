from copy import deepcopy

from typing import Optional

from back.configuration import BOARD_SIZE
from back.models.errors import AlreadyTakenPosition
from back.models.pieces import pieces_catalog
from back.models.pieces.piece_interface import Piece
from back.models.player.player import PLAYER
from back.models.pieces.piece_labels import PIECE_LABEL
from back.tool_box import is_in_bound

"""
For read me for back end 
Always use  x, y for methods or encapsulate them in a method

"""

class ChessModel:

    def __init__(self):
        self.board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.previous_model_state = None
        self.pieces = []
        self.allowed_moves = {}
        self.player_turn = PLAYER.PLAYER_1

    def update_player_turn(self):
        if self.player_turn == PLAYER.PLAYER_1:
            self.player_turn = PLAYER.PLAYER_2
        elif self.player_turn == PLAYER.PLAYER_2:
            self.player_turn = PLAYER.PLAYER_1

    def update_allowed_moves(self):
        _ = [piece.update_allowed_positions(self) for piece in self.pieces]
        self.allowed_moves = {piece: piece.allowed_positions for piece in self.pieces}

    def move_piece(self, destination_row: int, destination_col: int, piece: Piece):
        self.previous_model_state = deepcopy(self)
        position_content = self.get_position_content_from_indexes(destination_row, destination_col)
        if position_content is not None and position_content.player != piece.player:
            self.remove_piece(position_content)
        self.board[piece.row][piece.col] = None
        self.board[destination_row][destination_col] = piece
        piece.update_position(destination_row, destination_col)
        self.update_player_turn()

    def remove_piece(self, piece: Piece):
        self.board[piece.row][piece.col] = None
        self.pieces.remove(piece)
        del self.allowed_moves[piece]
        del piece

    def get_position_content_from_indexes(self, row: int, col: int) -> Optional[Piece]:
        if is_in_bound(row, col) and isinstance(self.board[row][col], Piece):
            return self.board[row][col]
        return None

    def add_piece(self, row, col, player, label):
        if self.get_position_content_from_indexes(row, col):
            raise AlreadyTakenPosition('There is a piece in this position, select an empty position')
        piece_class = pieces_catalog[label]
        piece = piece_class(row, col, player)
        self.board[piece.row][piece.col] = piece
        self.pieces.append(piece)
        return piece

    def undo(self):
        if self.previous_model_state:
            self.__dict__ = self.previous_model_state.__dict__

    def castle(self):
        raise NotImplementedError

    def fill_board(self):
        self.add_piece(row=3, col=4, player=PLAYER.PLAYER_1, label=PIECE_LABEL.PAWN)
        self.add_piece(row=3, col=5, player=PLAYER.PLAYER_1, label=PIECE_LABEL.PAWN)
        self.add_piece(row=5, col=3, player=PLAYER.PLAYER_2, label=PIECE_LABEL.PAWN)

    def run(self):
        self.fill_board()
        self.update_allowed_moves()

    def __repr__(self):
        column_widths = [max(len(str(item)) if item is not None else 0 for item in col) for col in zip(*self.board)]
        rows = []
        for row in self.board:
            formatted_row = " ".join(
                "{:<{}}".format(str(item) if item is not None else "0", width + 2) for item, width in
                zip(row, column_widths))
            rows.append(formatted_row)

        return '-' * 30 + "\n" + "\n".join(rows)


if __name__ == "__main__":
    chess_model = ChessModel()
    print(chess_model)
    row = 2
    col = 3
    piece = chess_model.add_piece(row=2, col=3, player=PLAYER.PLAYER_1, label=PIECE_LABEL.PAWN)
    print(chess_model)
    piece.allowed_positions = [(7, 4)]
    chess_model.move_piece(7, 4, piece=piece)
    print(chess_model)
    chess_model.undo()
    print(chess_model)


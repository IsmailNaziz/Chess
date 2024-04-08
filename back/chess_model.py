from copy import deepcopy

from typing import Optional

from back.configuration import BOARD_SIZE
from back.models.errors import AlreadyTakenPosition
from back.models.pieces import pieces_catalog
from back.models.pieces.piece_interface import Piece
from back.models.player.player import PLAYER

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
        self.player_turn = PLAYER.PLAYER_1.value

    def update_allowed_moves(self):
        _ = [piece.update_possible_positions() for piece in self.pieces]
        self.allowed_moves = {piece: piece.possible_positions for piece in self.pieces}

    def move_piece(self, destination_row: int, destination_col: int, piece: Piece):
        self.previous_model_state = deepcopy(self)
        self.board[piece.row][piece.col] = None
        self.board[destination_row][destination_col] = piece
        piece.update_position(destination_row, destination_col)

    def remove_piece(self, piece: Piece):
        self.board[piece.row][piece.col] = None
        self.pieces.remove(piece)
        del piece

    def get_piece_from_coordinates(self, row: int, col: int) -> Optional[Piece]:
        if isinstance(self.board[row][col], Piece):
            return self.board[row][col]
        return None

    def add_piece(self, row, col, player, label):
        if self.get_piece_from_coordinates(row, col):
            raise AlreadyTakenPosition('There is a piece in this position, select an empty position')
        piece_class = pieces_catalog[label]
        piece = piece_class(row, col, player)
        self.board[piece.row][piece.col] = piece
        self.pieces.append(piece)

    def undo(self):
        if self.previous_model_state:
            self.__dict__ = self.previous_model_state.__dict__

    def run(self):
        self.fill_board()
        self.update_allowed_moves()

    def fill_board(self):
        raise NotImplementedError

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
    from back.models.pieces.piece_labels import PIECE_LABEL
    chess_model = ChessModel()
    print(chess_model)
    row = 2
    col = 3
    chess_model.add_piece(row=2, col=3, player=1, label=PIECE_LABEL.PAWN)
    print(chess_model)
    piece = chess_model.get_piece_from_coordinates(row, col)
    piece.possible_positions = [(7, 4)]
    chess_model.move_piece(7, 4, piece=piece)
    print(chess_model)
    chess_model.undo()
    print(chess_model)


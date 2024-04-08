from typing import Optional

from back.configuration import BOARD_SIZE
from back.models.errors import AlreadyTakenPosition
from back.models.pieces.piece_interface import Piece
from back.models.pieces import pieces_catalog

"""
For read me for back end 
Always use  x, y for methods or encapsulate them in a method

"""

class Board:

    def __init__(self):
        self.board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def move_piece(self, destination_row, destination_col, piece: Piece):
        self.board[piece.row][piece.col] = None
        self.board[destination_row][destination_col] = piece
        piece.update_position(destination_row, destination_col)

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

    def __repr__(self):
        # Find the maximum length of elements in each column
        column_widths = [max(len(str(item)) if item is not None else 0 for item in col) for col in zip(*self.board)]

        # Create formatted rows
        rows = []
        for row in self.board:
            formatted_row = " ".join("{:<{}}".format(str(item) if item is not None else "0", width + 2) for item, width in zip(row, column_widths))
            rows.append(formatted_row)

        return "\n".join(rows)


if __name__ == "__main__":
    from back.models.pieces.piece_labels import PIECE_LABEL
    board = Board()
    print(board)
    row = 2
    col = 3
    board.add_piece(row=2, col=3, player=1, label=PIECE_LABEL.PAWN)
    print(board)
    piece = board.get_piece_from_coordinates(row, col)
    piece.possible_positions = [(3, 3)]
    board.move_piece(3, 3, piece=piece)
    print(board)



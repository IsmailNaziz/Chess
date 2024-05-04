from back.models.pieces.bishop import Bishop
from back.models.pieces.king import King
from back.models.pieces.knight import Knight
from back.models.pieces.pawn import Pawn
from back.models.pieces.queen import Queen
from back.models.pieces.rook import Rook

pieces_catalog = {
    Pawn.LABEL: Pawn,
    Bishop.LABEL: Bishop,
    Queen.LABEL: Queen,
    King.LABEL: King,
    Knight.LABEL: Knight,
    Rook.LABEL: Rook,
}


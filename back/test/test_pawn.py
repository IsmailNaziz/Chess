from unittest import TestCase

from back.chess_model import ChessModel
from back.models.pieces.piece_labels import PIECE_LABEL
from back.models.player.player import PLAYER


class TestPawn(TestCase):

    def test_possible_positions(self):
        chess_model = ChessModel()  # To be instantiated correctly
        row, col = 5, 4
        white_piece = chess_model.add_piece(row=row,
                                            col=col,
                                            player=PLAYER.PLAYER_1,
                                            label=PIECE_LABEL.PAWN)

        self.assertTrue(white_piece.possible_positions, [(6, 4)])

    def test_update_allowed_positions_not_right_turn(self):
        chess_model = ChessModel()
        piece = chess_model.add_piece(row=2, col=3, player=PLAYER.PLAYER_1, label=PIECE_LABEL.PAWN)
        chess_model.player_turn = PLAYER.PLAYER_2
        piece.update_allowed_positions()
        self.assertEqual(len(piece.allowed_positions), 0)

    def test_update_allowed_positions_filter_out_not_inbound_positions(self):
        chess_model = ChessModel()
        piece = chess_model.add_piece(row=2, col=3, player=PLAYER.PLAYER_1, label=PIECE_LABEL.PAWN)
        piece.allowed_positions.append((8, 9))
        piece.update_allowed_positions()
        self.assertEqual(len(piece.allowed_positions), 1)
        self.assertEqual(piece.allowed_positions[0], (1, 3))

    def test_update_allowed_positions_filter_out_taken_position_by_aly_positions(self):
        row, col = 6, 4
        destination_row, destination_col = 5, 4
        chess_model = ChessModel()
        white_piece = chess_model.add_piece(row=row,
                                            col=col,
                                            player=PLAYER.PLAYER_1,
                                            label=PIECE_LABEL.PAWN)
        # prerequisite of the test, the move should be in allowed positions before adding the piece
        chess_model.update_allowed_moves()
        self.assertTrue((6, 4) in white_piece.allowed_positions)

        # white piece in front
        chess_model.add_piece(row=destination_row,
                              col=destination_col,
                              player=PLAYER.PLAYER_1,
                              label=PIECE_LABEL.PAWN)
        chess_model.update_allowed_moves()
        self.assertTrue((6, 4) not in white_piece.allowed_positions)

    def test_possible_capture_positions(self):
        row, col = 6, 2
        chess_model = ChessModel()
        white_piece = chess_model.add_piece(row=row,
                                            col=col,
                                            player=PLAYER.PLAYER_1,
                                            label=PIECE_LABEL.PAWN)
        # prerequisite of the test, the move should be in allowed positions before adding the piece
        chess_model.update_allowed_moves()
        self.assertEqual(white_piece.possible_capture_positions, [(5, 1), (5, 3)])

    def test_capture_positions_in_allowed_position(self):
        row, col = 6, 2
        chess_model = ChessModel()
        white_piece = chess_model.add_piece(row=row,
                                            col=col,
                                            player=PLAYER.PLAYER_1,
                                            label=PIECE_LABEL.PAWN)
        # prerequisite of the test, the move should be in allowed positions before adding the piece
        chess_model.update_allowed_moves()
        self.assertEqual((5, 3) not in white_piece.allowed_positions)
        self.assertEqual((5, 1) not in white_piece.allowed_positions)

        black_piece = chess_model.add_piece(row=5,
                              col=3,
                              player=PLAYER.PLAYER_1,
                              label=PIECE_LABEL.PAWN)
        chess_model.update_allowed_moves()
        self.assertEqual((5, 3) in white_piece.allowed_positions)

        chess_model.remove_piece(black_piece)
        chess_model.add_piece(row=5,
                              col=1,
                              player=PLAYER.PLAYER_1,
                              label=PIECE_LABEL.PAWN)
        chess_model.update_allowed_moves()

        self.assertEqual((5, 1) in white_piece.allowed_positions)

    def test_end_to_end_update_allowed_positions(self):
        raise NotImplementedError

    def test_promote_pawn(self):
        # TODO after implementation of other pieces as the player selects the new piece
        # might be in another test class
        raise NotImplementedError

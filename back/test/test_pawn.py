from unittest import TestCase

from back.chess_model import ChessModel


class TestPawn(TestCase):


    def test_update_allowed_positions_not_right_turn(self):
        self.chess_model = ChessModel()  # To be instantiated correctly
        raise NotImplementedError

    def test_update_allowed_positions_filter_out_not_inbound_positions(self):
        self.chess_model = ChessModel()  # To be instantiated correctly
        raise NotImplementedError

    def test_update_allowed_positions_filter_out_taken_position_by_aly_positions(self):
        self.chess_model = ChessModel()  # To be instantiated correctly
        raise NotImplementedError

    def test_possible_positions(self):
        self.chess_model = ChessModel()  # To be instantiated correctly
        raise NotImplementedError

    def test_possible_capture_positions(self):
        self.chess_model = ChessModel()  # To be instantiated correctly
        raise NotImplementedError

    def test_promote_pawn(self):
        # TODO after implementation of other pieces as the player selects the new piece
        # might be in another test class
        raise NotImplementedError

    def test_valid_capture_positions(self):
        self.chess_model = ChessModel()  # To be instantiated correctly
        raise NotImplementedError

    def test_end_to_end_update_allowed_positions(self):
        raise NotImplementedError
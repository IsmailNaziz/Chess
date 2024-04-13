from copy import deepcopy
from unittest import TestCase

from back.chess_model import ChessModel
from back.models.errors import IllegalMoveError, AlreadyTakenPosition
from back.models.pieces import Pawn
from back.models.pieces.piece_labels import PIECE_LABEL
from back.models.player.player import PLAYER


class TestChessModel(TestCase):

    def test_update_player_turn(self):
        chess_model = ChessModel()
        previous_player_turn = chess_model.player_turn = PLAYER.PLAYER_1
        self.assertNotEqual(previous_player_turn, chess_model.player_turn)
        previous_player_turn = chess_model.player_turn = PLAYER.PLAYER_2
        chess_model.update_player_turn()
        self.assertNotEqual(previous_player_turn, chess_model.player_turn)

    def test_get_position_content_from_indexes(self):
        chess_model = ChessModel()
        row, col, player = 3, 6, PLAYER.PLAYER_1
        piece = Pawn(row, col, player)
        chess_model.board[row][col] = piece
        chess_model.pieces.append(piece)  # for consistency
        self.assertEqual(chess_model.get_position_content_from_indexes(row=row,
                                                                       col=col),
                         chess_model.board[row][col])
        with self.assertRaises(IndexError):
            row, col = 8, 8
            chess_model.get_position_content_from_indexes(row=row,
                                                          col=col)

    def test_add_piece_into_taken_position(self):
        row, col = 3, 6
        with self.assertRaises(AlreadyTakenPosition):
            chess_model = ChessModel()
            chess_model.add_piece(row=row,
                                  col=col,
                                  player=PLAYER.PLAYER_1,
                                  label=PIECE_LABEL.PAWN)
            chess_model.add_piece(row=row,
                                  col=col,
                                  player=PLAYER.PLAYER_1,
                                  label=PIECE_LABEL.PAWN)

    def test_add_piece_into_empty_position(self):
        chess_model = ChessModel()
        row, col = 3, 6
        piece = chess_model.add_piece(row=row,
                                      col=col,
                                      player=PLAYER.PLAYER_1,
                                      label=PIECE_LABEL.PAWN)
        # check update of piece attribute
        self.assertEqual(piece.row, row)
        self.assertEqual(piece.col, col)
        # consistency with the chess_model
        self.assertEqual(piece, chess_model.get_position_content_from_indexes(row, col))

    def test_move_piece_to_not_allowed_position(self):
        row, col = 3, 4
        destination_row, destination_col = 7, 7
        with self.assertRaises(IllegalMoveError):
            chess_model = ChessModel()
            # pawn is used arbitrarily, the values are tested in another place
            piece = chess_model.add_piece(row=row,
                                          col=col,
                                          player=PLAYER.PLAYER_1,
                                          label=PIECE_LABEL.PAWN)
            chess_model.move_piece(destination_row=destination_row,
                                   destination_col=destination_col,
                                   piece=piece)

    def test_move_piece_to_out_of_bound_with_not_allowed_position(self):
        row, col = 3, 4
        destination_row, destination_col = 8, 8
        with self.assertRaises(IndexError):
            chess_model = ChessModel()
            # pawn is used arbitrarily, the values are tested in another place
            piece = chess_model.add_piece(row=row,
                                          col=col,
                                          player=PLAYER.PLAYER_1,
                                          label=PIECE_LABEL.PAWN)
            chess_model.move_piece(destination_row=destination_row,
                                   destination_col=destination_col,
                                   piece=piece)

    def test_move_piece_to_out_of_bound_with_position_in_bound(self):
        row, col = 7, 4
        destination_row, destination_col = 8, 4
        with self.assertRaises(IndexError):
            chess_model = ChessModel()
            # pawn is used arbitrarily, the values are tested in another place
            piece = chess_model.add_piece(row=row,
                                          col=col,
                                          player=PLAYER.PLAYER_1,
                                          label=PIECE_LABEL.PAWN)
            chess_model.move_piece(destination_row=destination_row,
                                   destination_col=destination_col,
                                   piece=piece)

    def test_move_piece_without_capturing(self):
        row, col = 5, 4
        destination_row, destination_col = 6, 4
        chess_model = ChessModel()
        piece = chess_model.add_piece(row=row,
                                      col=col,
                                      player=PLAYER.PLAYER_1,
                                      label=PIECE_LABEL.PAWN)
        chess_model.move_piece(destination_row=destination_row,
                               destination_col=destination_col,
                               piece=piece)
        self.assertEqual(piece.row, destination_row)
        self.assertEqual(piece.col, destination_col)

    def test_move_piece_with_capturing(self):
        row, col = 5, 4
        destination_row, destination_col = 6, 4
        chess_model = ChessModel()
        white_piece = chess_model.add_piece(row=row,
                                            col=col,
                                            player=PLAYER.PLAYER_1,
                                            label=PIECE_LABEL.PAWN)
        chess_model.add_piece(row=destination_row,
                              col=destination_col,
                              player=PLAYER.PLAYER_2,
                              label=PIECE_LABEL.PAWN)
        chess_model.move_piece(destination_row=destination_row,
                               destination_col=destination_col,
                               piece=white_piece)
        self.assertTrue(white_piece.row == destination_row and white_piece.col == destination_col)

    def test_undo_without_capturing(self):
        # I couldn't understand why equality did not work
        # # initialization of variables
        # row, col = 5, 6
        # destination_row_1, destination_col_1 = 4, 6
        # destination_row_2, destination_col_2 = 3, 6
        # chess_model = ChessModel()
        #
        # # Adding a piece
        # piece = chess_model.add_piece(row=row,
        #                               col=col,
        #                               player=PLAYER.PLAYER_1,
        #                               label=PIECE_LABEL.PAWN)
        # # Moving a piece
        # expected_before_first_move = deepcopy(chess_model)
        # chess_model.move_piece(destination_row=destination_row_1,
        #                        destination_col=destination_col_1,
        #                        piece=piece)
        #
        # chess_model.update_player_turn()
        # # Moving a piece
        # expected_before_second_move = deepcopy(chess_model)
        # chess_model.move_piece(destination_row=destination_row_2,
        #                        destination_col=destination_col_2,
        #                        piece=piece)
        #
        # chess_model.undo()
        # self.assertEqual(chess_model.board, expected_before_second_move.board)
        # chess_model.undo()
        # self.assertEqual(chess_model, expected_before_first_move)
        raise NotImplementedError

    def test_undo_with_capturing(self):
        raise NotImplementedError

    def test_undo_with_no_previous_situation(self):
        raise NotImplementedError

    def test_remove_piece(self):
        row, col = 5, 4
        chess_model = ChessModel()
        piece = chess_model.add_piece(row=row,
                                      col=col,
                                      player=PLAYER.PLAYER_1,
                                      label=PIECE_LABEL.PAWN)
        chess_model.remove_piece(piece)
        self.assertTrue(chess_model.board[row][col] is None)
        self.assertTrue(piece not in chess_model.pieces)
        self.assertTrue(piece not in chess_model.allowed_moves)

    def test_fill_board(self):
        # TODO: after implementing other pieces
        raise NotImplementedError

    def test_castle(self):
        # TODO: after implementing other pieces
        raise NotImplementedError

    def test_update_allowed_moves(self):
        chess_model = ChessModel()
        white_row, white_col, white_player = 3, 6, PLAYER.PLAYER_1
        black_row, black_col, black_player = 6, 4, PLAYER.PLAYER_2
        white_piece = Pawn(white_row, white_col, white_player)
        black_piece = Pawn(black_row, black_col, black_player)
        chess_model.board[white_row][white_col] = white_piece
        chess_model.board[black_row][black_col] = black_piece
        chess_model.pieces.append(white_piece)
        chess_model.pieces.append(black_piece)
        allowed_moves_before_update = deepcopy(chess_model.allowed_moves)
        chess_model.update_allowed_moves()
        # Only checks if value changes
        self.assertNotEqual(allowed_moves_before_update, chess_model.allowed_moves)

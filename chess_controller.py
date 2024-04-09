from typing import Optional

from back.models.pieces.piece_interface import Piece
from front.configuration import UNDO_BUTTON_POSITION, BUTTON_SIZE

FPS = 60
from back.chess_model import ChessModel
from front.chess_view import ChessView
import pygame


class CheckerController:
    # connexion backend / frontend
    def __init__(self):
        self.chess_model = ChessModel()
        self.chess_view = ChessView()
        self.selected_piece = None


    def get_selected_cell_content(self, x, y) -> Optional[Piece]:
        selected_cell_row, selected_cell_col = self.chess_view.compute_board_indexes_from_position_on_window(x, y)
        return self.chess_model.board[selected_cell_row][selected_cell_col]

    def click_on_grid(self):
        clicked_position = pygame.mouse.get_pos()
        clicked_row, clicked_col = \
            self.chess_view.compute_board_indexes_from_position_on_window(*clicked_position)
        clicked_cell_content = self.chess_model.get_cell_content_from_indexes(clicked_row, clicked_col)

        if clicked_cell_content:
            # TODO: if enemy piece in cell content capture
            if clicked_cell_content != self.selected_piece:
                # select new piece
                self.selected_piece = clicked_cell_content
            else:
                # unselect piece after selection
                self.selected_piece = None
            return

        if not self.selected_piece:
            return

        # clicking on green spot
        if (clicked_row, clicked_col) in self.selected_piece.allowed_positions:
            self.chess_model.move_piece(clicked_row, clicked_col, self.selected_piece)
            self.selected_piece = None

    def undo_action(self, event):
        if pygame.Rect(*UNDO_BUTTON_POSITION, *BUTTON_SIZE).collidepoint(event.pos):
            self.chess_model.undo()
            self.selected_piece = None


    def run(self):
        self.chess_model.run()
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_on_grid()
                    self.undo_action(event)

            self.chess_view.update_grid(self.chess_model)
            if self.selected_piece:
                print(self.selected_piece)
                self.chess_view.display_allowed_moves(self.selected_piece, self.chess_model)
            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    check_controller = CheckerController()
    check_controller.run()

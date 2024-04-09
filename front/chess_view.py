import pygame
from back.configuration import BOARD_SIZE
from front.configuration import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME, WHITE, SQUARE_SIZE, BLUE, piece_image_catalog, \
    LIGHT_BLUE, MILD_WHITE, GREEN, GRAY, BLACK, FONT_SIZE, UNDO_BUTTON_POSITION, BUTTON_SIZE, RED, MENU_POSITION, \
    MENU_HEIGHT, MENU_WIDTH, BOARD_WIDTH, BOARD_HEIGHT


class ChessView:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_NAME)


    def draw_board(self):
        # pygame.draw.rect(self.window, WHITE, (0, 0, BOARD_WIDTH, BOARD_HEIGHT))
        for row in range(0, BOARD_SIZE):
            for col in range(0, BOARD_SIZE):
                color = LIGHT_BLUE if (row + col) % 2 != 0 else MILD_WHITE
                pygame.draw.rect(self.window, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_piece(self, piece):
        piece_position_on_window_x, piece_position_on_window_y = ChessView.compute_position_on_window_from_board_indexes(piece.row, piece.col)
        piece_image = piece_image_catalog[piece.player][piece.LABEL]
        # center image
        piece_position_on_window_x -= 50
        piece_position_on_window_y -= 55
        self.window.blit(piece_image, (piece_position_on_window_x, piece_position_on_window_y))

    def draw_pieces(self, chess_model):
        for piece in chess_model.pieces:
            self.draw_piece(piece)

    def draw_undo_button(self):
        button_rectangle = pygame.Rect(*UNDO_BUTTON_POSITION, *BUTTON_SIZE)

        button_color = BLUE if button_rectangle.collidepoint(pygame.mouse.get_pos()) else RED  # hover
        pygame.draw.rect(self.window, button_color, button_rectangle)

        undo_text = pygame.font.Font(None, FONT_SIZE).render('Undo', True, WHITE)
        self.window.blit(undo_text, (button_rectangle.x + BUTTON_SIZE[0] // 5,
                                     button_rectangle.y + BUTTON_SIZE[1] // 4))

    def draw_right_side_bar_menu_space(self):
        pygame.draw.rect(self.window, GRAY, (*MENU_POSITION, MENU_WIDTH, MENU_HEIGHT))
        pygame.draw.line(self.window, BLACK, start_pos=(BOARD_WIDTH, 0), end_pos=(BOARD_WIDTH, BOARD_HEIGHT), width=5)

    def draw_right_side_bar_menu(self):
        self.draw_right_side_bar_menu_space()
        # draw all elements of menu
        self.draw_undo_button()

    def update_grid(self, chess_model):
        self.draw_board()
        self.draw_right_side_bar_menu()
        self.draw_pieces(chess_model)



    def display_allowed_moves(self, selected_piece, chess_model):
        selected_piece_position_on_window = self.compute_position_on_window_from_board_indexes(selected_piece.row,
                                                                                               selected_piece.col)

        for allowed_move in chess_model.allowed_moves[selected_piece]:
            allowed_move_position = self.compute_position_on_window_from_board_indexes(*allowed_move)
            pygame.draw.circle(self.window, GREEN, allowed_move_position, 10)
        pygame.draw.circle(self.window, BLUE, selected_piece_position_on_window, 10)

    @staticmethod
    def compute_position_on_window_from_board_indexes(row, col):
        x = SQUARE_SIZE * col + SQUARE_SIZE // 2
        y = SQUARE_SIZE * row + SQUARE_SIZE // 2
        return x, y

    @staticmethod
    def compute_board_indexes_from_position_on_window(x, y):
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

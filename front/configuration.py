from pathlib import Path

import pygame
import os
from back.configuration import BOARD_SIZE
from back.models.pieces import Queen, King, Knight, Rook
from back.models.pieces.pawn import Pawn
from back.models.pieces.bishop import Bishop
from back.models.player.player import PLAYER

# BOARD SIZING
WINDOW_NAME = 'Chess game'
BOARD_HEIGHT = 800
BOARD_WIDTH = 800

# RIGHT SIDE BAR MENU
MENU_HEIGHT = 800
MENU_WIDTH = 130
MENU_POSITION = (BOARD_WIDTH, 0)

BUTTON_SIZE = (80, 30)
FONT_SIZE = 30
UNDO_BUTTON_POSITION = (BOARD_WIDTH + (MENU_WIDTH - BUTTON_SIZE[0]) // 2, (MENU_HEIGHT - BUTTON_SIZE[1]) // 2)

# WINDOW SIZING
WINDOW_HEIGHT = BOARD_HEIGHT
WINDOW_WIDTH = BOARD_WIDTH + MENU_WIDTH

# IMAGE LOADING
SQUARE_SIZE = BOARD_HEIGHT // BOARD_SIZE
PIECE_IMAGE_SCALE = (SQUARE_SIZE, SQUARE_SIZE)

parent_directory = Path(os.path.dirname(os.path.abspath(__file__)))
white_pieces_directory = 'assets/white_pieces'
black_pieces_directory = 'assets/black_pieces'
piece_image_catalog = {
    PLAYER.PLAYER_1: {
        Pawn.LABEL: pygame.transform.scale(
            pygame.image.load(parent_directory / white_pieces_directory / f'{Pawn.LABEL.value}.png'),
            PIECE_IMAGE_SCALE),
        Bishop.LABEL: pygame.transform.scale(
            pygame.image.load(parent_directory / white_pieces_directory / f'{Bishop.LABEL.value}.png'),
            PIECE_IMAGE_SCALE),
        Queen.LABEL: pygame.transform.scale(
            pygame.image.load(parent_directory / white_pieces_directory / f'{Queen.LABEL.value}.png'),
            PIECE_IMAGE_SCALE),
        King.LABEL: pygame.transform.scale(
            pygame.image.load(parent_directory / white_pieces_directory / f'{King.LABEL.value}.png'),
            PIECE_IMAGE_SCALE),
        Knight.LABEL: pygame.transform.scale(
            pygame.image.load(parent_directory / white_pieces_directory / f'{Knight.LABEL.value}.png'),
            PIECE_IMAGE_SCALE),
        Rook.LABEL: pygame.transform.scale(
            pygame.image.load(parent_directory / white_pieces_directory / f'{Rook.LABEL.value}.png'),
            PIECE_IMAGE_SCALE),
    },
    PLAYER.PLAYER_2: {
        Pawn.LABEL: pygame.transform.scale(
            pygame.image.load(parent_directory / black_pieces_directory / f'{Pawn.LABEL.value}.png'),
            PIECE_IMAGE_SCALE),
        Bishop.LABEL: pygame.transform.scale(
            pygame.image.load(parent_directory / black_pieces_directory / f'{Bishop.LABEL.value}.png'),
            PIECE_IMAGE_SCALE),
        Queen.LABEL: pygame.transform.scale(
            pygame.image.load(parent_directory / black_pieces_directory / f'{Queen.LABEL.value}.png'),
            PIECE_IMAGE_SCALE),
        King.LABEL: pygame.transform.scale(
            pygame.image.load(parent_directory / black_pieces_directory / f'{King.LABEL.value}.png'),
            PIECE_IMAGE_SCALE),
        Knight.LABEL: pygame.transform.scale(
            pygame.image.load(parent_directory / black_pieces_directory / f'{Knight.LABEL.value}.png'),
            PIECE_IMAGE_SCALE),
        Rook.LABEL: pygame.transform.scale(
            pygame.image.load(parent_directory / black_pieces_directory / f'{Rook.LABEL.value}.png'),
            PIECE_IMAGE_SCALE),
    }
}

# COLORS
MILD_WHITE = (237, 238, 230)
LIGHT_BLUE = (115, 151, 247)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

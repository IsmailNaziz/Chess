from back.configuration import BOARD_SIZE


def is_in_bound(row, col):
    return row >= 0 and row < BOARD_SIZE and col >= 0 and col < BOARD_SIZE


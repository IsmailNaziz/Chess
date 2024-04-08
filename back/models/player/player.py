from enum import Enum


class PLAYER(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2


class Player:
    """
    class created to handle remote players later
    """
    def __init__(self, player: PLAYER):
        self.player = player

from abc import ABC, abstractmethod
from typing import List, Callable

from back.models.errors import IllegalMoveError


class Piece(ABC):
    LABEL = None

    @abstractmethod
    def __init__(self):
        self.row = None
        self.col = None
        self.player = None
        self.allowed_positions = []

    @property
    def possible_positions(self):
        # corresponds to natural piece movement if nothing interferes
        return []

    @property
    def possible_capture_positions(self):
        # corresponds to positions that are only reachable when capturing other pieces
        return []

    @abstractmethod
    def update_allowed_positions(self, chess_model):
        """
        :param board: current board
        :param row: row of the piece in the board
        :param col: col of the piece in the board
        :return:
        modifies self.allowed_positions
        """
        pass

    def update_position(self, row, col) -> None:
        if (row, col) in self.allowed_positions:
            self.row = row
            self.col = col
        else:
            raise IllegalMoveError('You might have not updated the position of this piece, '
                                   'or you have made a mistake in possible move implementation')

    def __repr__(self):
        return self.LABEL.value

    def __str__(self):
        return self.LABEL.value

    def __format__(self, format_spec):
        return self.LABEL.value

    def __hash__(self):
        return hash(id(self))

    def __eq__(self, other):
        return hash(id(self)) == hash(id(other))

    def get_dial_filter_function(self, row, col) -> Callable:
        """
                         |
                    1    |    2
                         |
                ---------B---------
                         |
                     3   |    4
                         |
        returns the dial filter from given coordinates
        """

        if row <= self.row and col <= self.col:
            """
            *********|   |            
            *********|   |
           __________1   |    2
                         |
                ---------B---------
                         |
                     3   |    4
                         |
            the function filters out all the star zone ine dial 1
            """
            return lambda r, c: not (r <= row and c <= col)

        if row <= self.row and col >= self.col:
            return lambda r, c: not (r <= row and c >= col)

        if row >= self.row and col <= self.col:
            return lambda r, c: not (r >= row and c <= col)

        if row >= self.row and col >= self.col:
            return lambda r, c: not (r >= row and c >= col)

    def get_straight_line_filter_function(self, row, col) -> Callable:
        """
                         *
                         *
                         up
                         |
                **left---B-----right**
                         down
                         *
                         *
        returns the line filter from given coordinates
        """

        if row <= self.row and col == self.col:
            """     
                         *
                         *
                         up    
                         |
                ---------B---------
                         |
                         |  
                         |
            the function filters out all the star zone up
            """
            return lambda r, c: not (r <= row and c == col)

        if row >= self.row and col == self.col:
            """
                         |
                         |    
                         |
                ---------B---------
                         |
                         down  
                         *
                         *
            the function filters out all the star zone up
            """
            return lambda r, c: not (r >= row and c == col)

        if row == self.row and col >= self.col:
            """
                         |
                         |    
                         |
                ---------B------right**
                         |
                         | 
                         |
            the function filters out all the star zone up
            """
            return lambda r, c: not (r == row and c >= col)

        if row == self.row and col <= self.col:
            """
                         |
                         |    
                         |
                **left---B---------
                         |
                         | 
                         |
            the function filters out all the star zone up
            """
            return lambda r, c: not (r == row and c <= col)

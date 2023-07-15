"""
This file contains the core functionality for the Tic Tac Toe game.
"""
from enum import Enum
from typing import Optional


class Player(Enum):
    X = "X"
    O = "O"


def is_board_full(board: list[list[str]]) -> bool:
    """
    Check if the game board is full and no other move can be made.

    Returns:
        True if the game board is full, false otherwise.
    """
    return False


def check_winner(board: list[list[str]]) -> Optional[Player]:
    """
    Check if there is a winner for the given game board.

    Returns:
        None if there is no winner, otherwise returns the winning Player.
    """
    return None

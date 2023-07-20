"""
This file contains the core functionality for the Tic Tac Toe game.
"""
from enum import Enum
from typing import Optional

BOARD_SIZE = 3


class Player(Enum):
    X = "X"
    O = "O"


def is_board_full(board: list[list[str]]) -> bool:
    """
    Check if the game board is full and no other move can be made.

    Returns:
        True if the game board is full, false otherwise.
    """
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == "":
                return False
    return True


def check_winner(board: list[list[str]]) -> Optional[Player]:
    """
    Check if there is a winner for the given game board.
    Returns:
        None if there is no winner, otherwise returns the winning Player.
    """

    # Check rows:
    for i in range(BOARD_SIZE):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return Player(board[i][0])

    # Check cols:
    for j in range(BOARD_SIZE):
        if board[0][j] == board[1][j] == board[2][j] != "":
            return Player(board[0][j])

    # check diagonals:
    if board[0][0] == board[1][1] == board[2][2] != "":
        return Player(board[0][0])
    if board[0][2] == board[1][1] == board[2][0] != "":
        return Player(board[0][2])

    return None

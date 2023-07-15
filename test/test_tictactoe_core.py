from src.tictactoe_core import check_winner
from src.tictactoe_core import Player


def test_check_winner() -> None:
    B1 = [["X", "", ""], ["", "X", "O"], ["O", "", "X"]]
    assert check_winner(B1) == Player.X

    B2 = [["X", "", ""], ["", "", "O"], ["", "", ""]]
    assert check_winner(B2) == None

    # Please write a few more test cases.


def test_is_board_full() -> None:
    # Please write your test here.
    pass

from src.tictactoe_core import check_winner
from src.tictactoe_core import is_board_full
from src.tictactoe_core import Player


def test_check_winner() -> None:
    B1 = [["X", "", ""], ["", "X", "O"], ["O", "", "X"]]
    assert check_winner(B1) == Player.X

    B2 = [["X", "", ""], ["", "", "O"], ["", "", ""]]
    assert check_winner(B2) == None
    # Please write a few more test cases.
    B3 = [["X", "X", "X"], ["", "", ""], ["O", "O", ""]]
    assert check_winner(B3) == Player.X

    B4 = [["X", "O", ""], ["X", "O", ""], ["X", "", ""]]
    assert check_winner(B4) == Player.X

    B5 = [["O", "O", ""], ["X", "X", "X"], ["O", "X", "O"]]
    assert check_winner(B5) == Player.X

    B6 = [["O", "X", "O"], ["X", "X", "O"], ["O", "O", "X"]]
    assert check_winner(B6) == None

    B7 = [["O", "", "X"], ["O", "X", ""], ["O", "", ""]]
    assert check_winner(B7) == Player.O

    B8 = [["X", "X", "O"], ["O", "X", "O"], ["X", "O", "X"]]
    assert check_winner(B8) == Player.X

    B9 = [["X", "O", "X"], ["O", "O", "X"], ["X", "X", "O"]]
    assert check_winner(B9) == None


def test_is_board_full() -> None:
    # Please write your test here.
    B1 = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
    assert is_board_full(B1) is True

    B2 = [["X", "O", ""], ["O", "", "O"], ["O", "X", "O"]]
    assert is_board_full(B2) is False

    B3 = [["X", "", ""], ["", "O", ""], ["O", "", "X"]]
    assert is_board_full(B3) is False

    B4 = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "O"]]
    assert is_board_full(B4) is True

    B5 = [["O", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]
    assert is_board_full(B5) is True


test_is_board_full()

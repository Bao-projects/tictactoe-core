from src.tictactoe_core import check_winner
from src.tictactoe_core import is_board_full
from src.tictactoe_core import is_board_valid
from src.tictactoe_core import Player


# TODO: implement test case for is_board_valid
def test_is_board_valid() -> None:
    
    #valid boards:
    B1 = [["X", "", ""], ["", "X", "O"], ["O", "", "X"]]
    assert test_is_board_valid(B1)
    
    B2 = [["X", "", ""], ["", "", "O"], ["", "", ""]]
    assert test_is_board_valid(B2)
    
    B3 = [["X", "O", "X"], ["O", "X", "O"], ["", "X", "O"]]
    assert test_is_board_valid(B3)
    
    #invalid boards:
    B4 = [["X", "", ""], ["", "Y", "O"], ["O", "", "X"]] #invalid input
    assert not is_board_valid(B4)
      
    B5 = [["X", "", ""], ["", "X", "O"], ["X","X","O"]] # not by turn
    assert not is_board_valid(B5)
    
    B6 = [["X", "X", "O"], ["O", "O", "O"], ["X", "X", "X"]]#both winning
    assert not is_board_valid(B6)
    
    B7 = [["X", "X"], ["O", "O"]]  #invalid size not 3x3
    assert not is_board_valid(B7)
    
    pass

def test_check_winner() -> None:
    B1 = [["X", "", ""], ["", "X", "O"], ["O", "", "X"]]
    assert check_winner(B1) == Player.X

    B2 = [["X", "", ""], ["", "", "O"], ["", "", ""]]
    assert check_winner(B2) == None

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
    B1 = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
    assert is_board_full(B1)

    B2 = [["X", "O", ""], ["O", "", "O"], ["O", "X", "O"]]
    assert not is_board_full(B2)

    B3 = [["X", "", ""], ["", "O", ""], ["O", "", "X"]]
    assert not is_board_full(B3)

    B4 = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "O"]]
    assert is_board_full(B4)

    B5 = [["O", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]
    assert is_board_full(B5)

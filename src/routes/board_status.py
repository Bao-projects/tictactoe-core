import json

from flask import request

from . import routes
from src.routes.helper.responses import BoardStatusResult
from src.routes.helper.responses import FailureResult
from src.tictactoe_core import check_winner
from src.tictactoe_core import is_board_full
from src.tictactoe_core import is_board_valid


@routes.route("/board_status", methods=["GET"])
def board_status():
    board = json.loads(request.form["board"])
    board_valid = is_board_valid(board)

    if not board_valid:
        return FailureResult("Invalid board").to_flask_response()

    winner = check_winner(board)
    has_winner = winner is not None
    return BoardStatusResult(
        is_board_full(board), has_winner, winner
    ).to_flask_response()

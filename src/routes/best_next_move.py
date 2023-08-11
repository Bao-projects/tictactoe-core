import json

from flask import request

from . import routes
from src.routes.helper.responses import BestNextMoveResult
from src.routes.helper.responses import FailureResult
from src.tictactoe_core import best_next_move


@routes.route("/best_next_move", methods=["GET"])
def next_move():
    """
    next_move REST API, support GET requests only.
    This API will take in an 3D array at the current board status
    and the current player turn.
    Returns:
        The move of the current player and the coordination
        of that move from the result of best_next_move.
    """
    board = json.loads(request.form["board"])
    for_player = request.form["player"]
    if for_player not in ["X", "O"]:
        return FailureResult("Invalid input").to_flask_response()

    next_move = best_next_move(board, for_player)
    return BestNextMoveResult(next_move).to_flask_response()

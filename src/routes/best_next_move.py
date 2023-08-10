import json

from flask import request

from . import routes
from src.routes.helper.responses import BestNextMoveResult
from src.tictactoe_core import best_next_move


@routes.route("/best_next_move", methods=["GET"])
def next_move():
    board = json.loads(request.form["board"])
    print(board)

    for_player = request.form["player"]
    print(for_player)

    next_move = best_next_move(board, for_player)
    return BestNextMoveResult(for_player, next_move).to_flask_response()

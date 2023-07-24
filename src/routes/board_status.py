from . import routes


@routes.route("/board_status", methods=["GET"])
def board_status():
    """
    board_status REST API, support GET requests only.
    This API will take in a 2D array as the representation of the tic tac toe
    board, and will return a result of the board status (including whether the
    board is full, whether there is a winner, and if there is a winner then
    who is the winner). In case the tic tac toe board is invalid, it will return
    an error message along with response code of 400
    """

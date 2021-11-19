import AI_opponent
import game_board
import ships

"""
Main game play
"""

def players_turn(active_player):
    """
    This function takes the active player's input shot
    """

    pass


def checking_result(active_player):
    """
    This function determines the outcome of the active player's turn
    :param active_player: the player who's input their turn
    :return: The message of Hit (possible Sink) or Miss.
    """

    pass


while True:
    play = input("Let's play? Y/N : ")
    if play.upper() == "Y":
        player1 = game_board.player1_table()
        player2 = game_board.player2_table()
        game_board.display_one_grid(player1)
        ships.placement(player1)
        ships.placement(AI_opponent.ai_placement(player2))
        print("\n\n\n Let's start battle!")


    else:
        print("Ok see you another time.")
        break





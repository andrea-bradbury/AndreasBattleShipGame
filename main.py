import AI_opponent
import game_board
import ships




def players_turn(inactive_player_table):
    """
    This function takes the active player's turn and returns a message of whether the player
    Hit, Missed or Sunk.

    :return: the message for the active player on their turn
    """

    active_players_shot = input("Enter your shot on your opponent: ")

    alph_value = active_players_shot[0].upper()
    num_value, test = ships.intTryParse(active_players_shot[1:])

    if test and (10 >= num_value > 0):
        if alph_value in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
            if (inactive_player_table[alph_value][num_value-1] == "O") or (inactive_player_table[alph_value][num_value-1] == "X"):
                message = "You've already shot here."

            elif inactive_player_table[alph_value][num_value-1] == " ":
                message = "You missed."
                inactive_player_table[alph_value][num_value-1] = "O"
                print(inactive_player_table)

            else:
                message = "You hit a ship!"
                inactive_player_table[alph_value][num_value - 1] = "X"
                print(inactive_player_table)

        else:
            message = "Check your position entry."



    return print(message)


def checking_result():
    """
    This function checks if either player has won and returns the status of the game / winner.
    """

    #Check if player 1 has won
    player1_number_of_hits = 0
    for item in player1.items():
        for i in item:
            for y in i:
                if y == 'X':
                    player1_number_of_hits += 1

    #Check if player 2 has won
    player2_number_of_hits = 0
    for item in player2.items():
        for i in item:
            for y in i:
                if y == 'X':
                    player2_number_of_hits += 1

    #determine status and winner
    if player2_number_of_hits == 27 or player1_number_of_hits == 27:
        game_status = "Game Over"
        if player2_number_of_hits == 27:
            winner = "Player 1"
        else:
            winner = "Player 2"

    else:
        game_status = "Keep playing"
        winner = ""


    return game_status, winner


"""
Main game play
"""


play = input("Let's play? Y/N : ")
if play.upper() == "Y":

    #The game boards are held here
    player1 = game_board.player1_table()
    player2 = game_board.player2_table()

    #Player 1 placing ships on board
    game_board.display_one_grid(player1)
    ships.placement(player1)
    print(player1)

    #player 2 placing ships on board
    game_board.display_one_grid(player2)
    AI_opponent.ai_placement(player2)
    print(player2)

    print("\n\n\n Let's start battle!")
    game_board.display_two_grids(player1, player2)

    players = [player1, player2]
    game_status, winner = checking_result()
    #Taking turns firing
    while game_status == "Keep playing":
        opponent = players[1]
        print("\n\nPLAYER 1: ")
        players_turn(opponent)
        game_board.display_two_grids(players[0], players[1])
        game_status, winner = checking_result()
        if game_status == "Game Over":
            break
        else:
            opponent = players[0]
            print("\n\nPLAYER 2: ")
            players_turn(opponent)
            game_board.display_two_grids(players[0], players[1])
            game_status, winner = checking_result()
            if game_status == "Game Over":
                break

    print(game_status + " \n\n" + winner + "is the winner")


else:
    print("Ok see you another time.")






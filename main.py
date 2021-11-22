import second_player
import game_board
import ships


def players_turn(inactive_player_table):
    """
    This function takes the active player's turn and returns a message of whether the player
    Hit or Missed.

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

            else:
                message = "You hit a ship!"
                inactive_player_table[alph_value][num_value - 1] = "X"

        else:
            message = "Check your position entry."

    return print(message)


def checking_result():
    """
    This function checks if either player has won and returns the status of the game & winner if there is one.
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
Main game play is written below. 
This game allows for two human players to play each other. 
It assumes that while the active player is taking their turn, the inactive player cannot look at the screen.

"""

play = input("Let's play? Y/N : ")
if play.upper() == "Y":

    #The game boards for both players are held here
    player1 = game_board.player1_table()
    player2 = game_board.player2_table()
    #Used for determining who's turn it is
    players = [player1, player2]

    #Player 1 placing ships on board
    print("\nPLAYER 1 ENTER YOUR SHIPS")
    game_board.display_one_grid(player1)
    ships.placement(player1)

    #Player 2 placing ships on board
    print("\n\n\n PLAYER 2 ENTER YOUR SHIPS")
    game_board.display_one_grid(player2)
    second_player.second_player_placement(player2)

    print("\n\n\n Let's start battle!")

    #Just a safety check for testing
    game_status, winner = checking_result()

    #This loop will continue until the checking_results function returns a winner
    #Players take turns firing
    while game_status == "Keep playing":
        opponent = players[1]
        print("\n\n\n PLAYER 1...")
        #Display the table for player 1
        #You can use the function display_two_grids(player1, player2) for testing if you want to see where the opponent has placed their ships
        game_board.display_two_grids_opponent_blank(player1, player2)
        print("\n\nPLAYER 1: ")
        #This function accepts player 1's turn and returns the outcome of that fire
        players_turn(opponent)
        #The outcome is displayed on the table
        game_board.display_two_grids_opponent_blank(players[0], players[1])
        #Check if anyone has won from this turn
        game_status, winner = checking_result()
        if game_status == "Game Over":
            break
        else:
            opponent = players[0]
            print("\n\n\nPLAYER 2...")
            # Display the table for player 2
            # You can use the function display_two_grids(player1, player2) for testing if you want to see where the opponent has placed their ships
            game_board.display_two_grids_opponent_blank(players[1], players[0])
            print("\n\nPLAYER 2: ")
            # This function accepts player 2's turn and returns the outcome of that fire
            players_turn(opponent)
            # The outcome is displayed on the table
            game_board.display_two_grids_opponent_blank(players[1], players[0])
            # Check if anyone has won from this turn
            game_status, winner = checking_result()
            if game_status == "Game Over":
                break
    #Print outcome of game
    print("\n\n\n\n" + game_status + " \n\n" + winner + " is the winner")

else:
    print("Ok see you another time.")






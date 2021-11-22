"""
This file deals only with displaying the front end game board(s) and collecting information for the back end game boards.

It contains:
 1. A function for displaying just 1 table (for players set up of ships)
 2. A function for displaying 2 tables (all ships visible) which is for testing
 3. A function for displaying 2 tables (only active player's table is fully visible and the opponent's table only shows hits and misses).
 4. Dictionaries for the back end tables for each player.
"""

def display_two_grids(player1, player2):
    """
    Displays grid to console
    Used for testing only. You can see your opponent's ships on this grid.
    """
    table_head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\n\n\n" + " " * 25 + " Your Table" + " " * 80 + "Opponent Board")
    print(" " * 5, end="|")

    # Grid Header
    for i in table_head:
        print(f"{i:^5}", end="|")
    print(" " * 24, end="|")
    for i in table_head:
        print(f"{i:^5}", end="|")

    # Grid Table
    for key in player1:
        print(f"\n\n{key:^5}", end="|")
        for item in player1[key]:
            print(f"{item:^5}", end="|")

        print(" " * 20, end="")
        print(key, end="   |")

        for item in player2[key]:
            print(f"{item:^5}", end="|")


def display_one_grid(player):
    """
    Display Grid to console. Used for set up of placing ships.
    """
    table_head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\n\n\n" + " " * 25 + "Game Board")
    print(" " * 5, end="|")

    # Grid Header
    for i in table_head:
        print(f"{i:^5}", end="|")



    # Grid Table
    for key in player:
        print(f"\n\n{key:^5}", end="|")
        for item in player[key]:
            print(f"{item:^5}", end="|")


def player1_table():
    """
    Dictionary for table grid.
    """
    return {"A": [" "] * 10,
            "B": [" "] * 10,
            "C": [" "] * 10,
            "D": [" "] * 10,
            "E": [" "] * 10,
            "F": [" "] * 10,
            "G": [" "] * 10,
            "H": [" "] * 10,
            "I": [" "] * 10,
            "J": [" "] * 10, }


def player2_table():
    return {"A": [" "] * 10,
            "B": [" "] * 10,
            "C": [" "] * 10,
            "D": [" "] * 10,
            "E": [" "] * 10,
            "F": [" "] * 10,
            "G": [" "] * 10,
            "H": [" "] * 10,
            "I": [" "] * 10,
            "J": [" "] * 10, }


def display_two_grids_opponent_blank(player1, player2):
    """
    Display Grid to console. This function is used for the real game so you cannot see your opponent's ships until you hit them.
    You can also track misses.
    """
    table_head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\n\n\n" + " " * 25 + " Your Table" + " " * 80 + "Opponent Board")
    print(" " * 5, end="|")

    # Grid Header
    for i in table_head:
        print(f"{i:^5}", end="|")
    print(" " * 24, end="|")
    for i in table_head:
        print(f"{i:^5}", end="|")

    # Grid Table
    for key in player1:
        print(f"\n\n{key:^5}", end="|")
        for item in player1[key]:
            print(f"{item:^5}", end="|")

        print(" " * 20, end="")
        print(key, end="   |")

        for item in player2[key]:
            if item == " " or item == "X" or item == "O":
                print(f"{item:^5}", end="|")
            else:
                print("     ", end="|")
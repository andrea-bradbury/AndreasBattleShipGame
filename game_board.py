def display_two_grids(player, opponent):
    """
    Display Grid to console
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
    for key in player:
        print(f"\n\n{key:^5}", end="|")
        for item in player[key]:
            print(f"{item:^5}", end="|")

        print(" " * 20, end="")
        print(key, end="   |")

        for item in opponent[key]:
            print(f"{item:^5}", end="|")


def display_one_grid(player):
    """
    Display Grid to console
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
    Dictionary for table grid
    """
    return {"A": [" "] * 10, "B": [" "] * 10, "C": [" "] * 10, "D": [" "] * 10, "E": [" "] * 10,
            "F": [" "] * 10, "G": [" "] * 10, "H": [" "] * 10, "I": [" "] * 10, "J": [" "] * 10, }


def player2_table():
    return {"A": [" "] * 10, "B": [" "] * 10, "C": [" "] * 10, "D": [" "] * 10, "E": [" "] * 10,
            "F": [" "] * 10, "G": [" "] * 10, "H": [" "] * 10, "I": [" "] * 10, "J": [" "] * 10, }
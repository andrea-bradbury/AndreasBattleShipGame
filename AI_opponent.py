import ships
import random

def ai_placement(player2):
    player2 = player2
    boat_number = 0
    max_ship = 10

    placing = True

    while placing:
        placing_direction = True
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ship_position = letters[random.randint(1, 9)] + str(numbers[random.randint(1, 9)])


        #Don't need to validate letter in bounds to upper or int between 1-10
        alp_value = ship_position[0]
        num_value = ship_position[1:]


        while placing_direction:
            directions = [1, 2, 3, 4]
            ship_direction = directions[random.randint(1, 3)]
            #Don't need to validate as an int in range

            boat_type = ["PB", "PB", "D", "D", "C", "S", "S", "S", "B", "AC"]
            player2, place = place_ship(player2, alp_value, int(num_value), ship_direction, boat_type[boat_number])
            if place:
                boat_number += 1
                if boat_number == max_ship:
                    placing = False
                    ships.display_one_grid(player2)
                    break
            else:
                placing_direction = False

    print("\n\n\n Your AI opponent has finished placing their ships.")

    return player2



def place_ship(table, alp_value, num_value, direction, boat_type):
    """Checks for ship placement overlaps and assign ships Tag to grid
        direction value 1.Left 2.Right 3.Top 4.Bottom
    """
    location = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    vector_alpha_location = 0
    for i in range(len(location)):
        if location[i] == alp_value:
            vector_alpha_location = i

    if boat_type == "PB":
        if table[alp_value][num_value - 1] == " ":
            table[alp_value][num_value - 1] = boat_type
        else:
            print("There is not enough room to place ship at this location")
            return table, False

    elif boat_type == "D":
        if direction == 1:
            if num_value - 1 < 1:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value - 2] == " ":

                ships.place_ship_left_right(table, boat_type, alp_value, num_value, 2, 1)
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 2:
            if num_value + 1 > 10:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value] == " ":

                ships.place_ship_left_right(table, boat_type, alp_value, num_value, 2, 2)

            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 3:
            for up in range(len(location)):
                if alp_value == location[up]:
                    if up - 1 < 1:
                        print("Ship cannot be place outside of grid")
                        return table, False

            if ships.check_free_space_top_bot(table, alp_value, num_value, location, vector_alpha_location, 2, 3):
                ships.place_ship_top_bot(table, boat_type, alp_value, num_value, location, vector_alpha_location, 2, 3)
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        else:
            for down in range(len(location)):
                if alp_value == location[down]:
                    if down + 1 > 10:
                        print("Ship cannot be place outside of grid")
                        return table, False

            if ships.check_free_space_top_bot(table, alp_value, num_value, location, vector_alpha_location, 2, 4):
                ships.place_ship_top_bot(table, boat_type, alp_value, num_value, location, vector_alpha_location, 2, 4)
            else:
                print("There is not enough room to place ship at this location")
                return table, False

    elif boat_type == "C" or boat_type == "S":
        if direction == 1:
            if num_value - 2 < 1:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value - 2] == " " and table[alp_value][
                    num_value - 3] == " ":

                ships.place_ship_left_right(table, boat_type, alp_value, num_value, 3, 1)
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 2:
            if num_value + 2 > 10:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value] == " " and table[alp_value][
                    num_value + 1] == " ":

                ships.place_ship_left_right(table, boat_type, alp_value, num_value, 3, 2)
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 3:
            for up in range(len(location)):
                if alp_value == location[up]:
                    if up - 2 < 1:
                        print("Ship cannot be place outside of grid")
                        return table, False

            if ships.check_free_space_top_bot(table, alp_value, num_value, location, vector_alpha_location, 3, 3):

                ships.place_ship_top_bot(table, boat_type, alp_value, num_value, location, vector_alpha_location, 3, 3)
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        else:
            for down in range(len(location)):
                if alp_value == location[down]:
                    if down + 2 > 10:
                        print("Ship cannot be place outside of grid")
                        return table, False
            if ships.check_free_space_top_bot(table, alp_value, num_value, location, vector_alpha_location, 3, 4):

                ships.place_ship_top_bot(table, boat_type, alp_value, num_value, location, vector_alpha_location, 3, 4)
            else:
                print("There is not enough room to place ship at this location")

    elif boat_type == "B":
        if direction == 1:
            if num_value - 3 < 1:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value - 2] == " " and table[alp_value][
                    num_value - 3] == " " and table[alp_value][num_value - 4] == " ":
                ships.place_ship_left_right(table, boat_type, alp_value, num_value, 4, 1)
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 2:
            if num_value + 3 > 10:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value] == " " and table[alp_value][
                    num_value + 1] == " " and table[alp_value][num_value + 2] == " ":
                ships.place_ship_left_right(table, boat_type, alp_value, num_value, 4, 2)
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 3:
            for up in range(len(location)):
                if alp_value == location[up]:
                    if up - 3 < 1:
                        print("Ship cannot be place outside of grid")
                        return table, False
            if ships.check_free_space_top_bot(table, alp_value, num_value, location, vector_alpha_location, 4, 3):
                ships.place_ship_top_bot(table, boat_type, alp_value, num_value, location, vector_alpha_location, 4, 3)
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        else:
            for down in range(len(location)):
                if alp_value == location[down]:
                    if down + 3 > 10:
                        print("Ship cannot be place outside of grid")
                        return table, False
            if ships.check_free_space_top_bot(table, alp_value, num_value, location, vector_alpha_location, 4, 4):

                ships.place_ship_top_bot(table, boat_type, alp_value, num_value, location, vector_alpha_location, 4, 4)
            else:
                print("There is not enough room to place ship at this location")

    elif boat_type == "AC":
        if direction == 1:
            if num_value - 4 < 1:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value - 2] == " " and table[alp_value][
                num_value - 3] == " " and table[alp_value][num_value - 4] == " " \
                    and table[alp_value][num_value - 5] == " ":

                ships.place_ship_left_right(table, boat_type, alp_value, num_value, 5, 1)
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 2:
            if num_value + 4 > 10:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value] == " " and table[alp_value][
                num_value + 1] == " " and table[alp_value][num_value + 2] == " " \
                    and table[alp_value][num_value + 3] == " ":

                ships.place_ship_left_right(table, boat_type, alp_value, num_value, 5, 2)
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 3:
            for up in range(len(location)):
                if alp_value == location[up]:
                    if up - 4 < 1:
                        print("Ship cannot be place outside of grid")
                        return table, False

            if ships.check_free_space_top_bot(table, alp_value, num_value, location, vector_alpha_location, 5, 3):

                ships.place_ship_top_bot(table, boat_type, alp_value, num_value, location, vector_alpha_location, 5, 3)
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        else:
            for down in range(len(location)):
                if alp_value == location[down]:
                    if down + 4 > 10:
                        print("Ship cannot be place outside of grid")
                        return table, False
            if ships.check_free_space_top_bot(table, alp_value, num_value, location, vector_alpha_location, 5, 4):

                ships.place_ship_top_bot(table, boat_type, alp_value, num_value, location, vector_alpha_location, 5, 4)
            else:
                print("There is not enough room to place ship at this location")
    return table, True



def players_turn(inactive_player_table):
    """
    This function takes the active player's turn and returns a message of whether the player
    Hit, Missed or Sunk.

    :return: the message for the active player on their turn
    """

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    active_players_shot = letters[random.randint(1, 9)] + str(numbers[random.randint(1, 9)])


    # Don't need to validate letter in bounds to upper or int between 1-10
    alp_value = active_players_shot[0]
    num_value = active_players_shot[1:]

    if (inactive_player_table[alp_value][int(num_value)-1] == "O") or (inactive_player_table[alp_value][int(num_value)-1] == "X"):
        message = "You've already shot here."

    elif inactive_player_table[alp_value][int(num_value)-1] == " ":
        message = "AI missed."
        inactive_player_table[alp_value][int(num_value)-1] = "O"
        print(inactive_player_table)

    else:
        message = "AI hit a ship!"
        inactive_player_table[alp_value][int(num_value) - 1] = "X"
        print(inactive_player_table)


    return active_players_shot, message


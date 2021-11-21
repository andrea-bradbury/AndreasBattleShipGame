import ships

def second_player_placement(player2):
    player2 = player2
    boat_number = 0
    max_ship = 10

    placing = True

    while placing:
        placing_direction = True
        ship_position = input(f"\n\n\nPlayer 2 where would you like to place your {ships.type_of_ships[boat_number]}: ")
        if ship_position == "":
            ship_position = "default wrong entry"
        alp_value = ship_position[0].upper()
        num_value, test = ships.intTryParse(ship_position[1:])
        if test and (10 >= num_value > 0):
            if alp_value in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                while placing_direction:
                    print("\nShip Direction:")
                    print("1.Left  |  2.Right  |  3.Top  |  4.Bottom")
                    print("Choose ship direction, Input Example: 2")
                    ship_direction = input("Enter ship direction in Number Value: ")
                    direction, test = ships.intTryParse(ship_direction)
                    if test and (4 >= direction > 0):
                        print("Good")
                        # working on detecting already placed ships
                        boat_type = ["PB", "PB", "D", "D", "C", "S", "S", "S", "B", "AC"]
                        player2, place = ships.place_ship(player2, alp_value, num_value, direction, boat_type[boat_number])
                        if place:
                            boat_number += 1
                            if boat_number == max_ship:
                                placing = False
                            ships.display_one_grid(player2)
                            break
                        else:
                            placing_direction = False
                    else:
                        print("Incorrect Input")
            else:
                print("Please Use Value between A-J and 1-10: Example Input: A2, J10, G5")
        else:
            print("Please Use Value between A-J and 1-10: Example Input: A2, J10, G5")
    return player2
# AndreasBattleShipGame

Aim: To build a fully functional game of battleships in python that is played within the console. 

This project has two versions: 
1. A two human players game 
2. A one human player, one AI player game

# Two human players game

To play, run main.py

Start the game and player 1 is invited to place their ships on the board using grid locations (A10, G4 ect)
They are then prompted to enter the direction they want this ship to face (1. Left, 2.Right, 3. Top, 4. Bottom)
They continue until all their ships have been placed correctly. 

Player 2 then does the same as player 1. 

The battle begins!

Each player takes turns entering a location to fire on, and the game provides a message of success or failure to hit a ship.

This continues until one player has hit all of their opponent's ships. (This does mean that player 1 has a small advantage going first).

The game displays the end of the game and the winner.


# One human player, one AI player game

To play run main_AI.py

Start the game and player 1 (the human) is invited to place their ships on the board using grid locations (A10, G4 ect)
They are then prompted to enter the direction they want this ship to face (1. Left, 2.Right, 3. Top, 4. Bottom)
They continue until all their ships have been placed correctly. 

Player 2 (the AI) uses the same framework to plot their ships but the locations are randomly generated using random.randint()

The battle begins!

Player one enters their fire location on their opponent. A message of success or failure is provided. 

The AI randomly picks locations on the board using random.randint(). 
Note: This AI will need to be improved to add logic around what happens when you get a hit.
Humans know that the chances of there being another hit within a space of the previous hit are much higher than a random spot on the board. 

This continues until one player has hit all of their opponent's ships. (This does mean that player 1 has a small advantage going first).

The game displays the end of the game and the winner.


# Notes: 
As part of the requirements of this project I have identified open source code which I have adapted for my project. 
The ships.py and game_board.py files are based upon the excellent work of Vushesh Dookheea https://github.com/VusheshDookheea , sourced November 2021.
This code was collected and used under the MIT license. 
When writing my AI opponent I discovered some small bugs in this code, which I will fix in the AI_opponent.py file.

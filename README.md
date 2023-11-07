# Tic Tac Toe Game (3x3)

This is a simple implementation of the classic Tic Tac Toe (3x3) game in Python. The game supports a user and a CPU player.

## Functions Documentation

### `user_turn(board)`

This function allows the user to make a move in the game. The user is prompted to enter the row and column numbers where they want to place their symbol (1). The function updates the game board accordingly.

### `cpu_turn(board, n)`

The `cpu_turn` function is responsible for the CPU's move. It aims to play optimally and considers potential winning moves for both the user and the CPU. It follows these steps:
- Checks if the CPU can make a winning move in a row, column, or diagonal. If so, it makes that move.
- If the user is about to win (with one move left to victory), it blocks the user's winning move.
- If none of the above conditions are met, the CPU places its symbol (2) in an empty cell on the game board randomly. If all cells are occupied, it declares a draw.

### `row_winner(board)`

This function checks if there is a winner in any row. It returns `True` if any row contains the same symbols (either 1 or 2), indicating a win.

### `column_winner(board, n)`

Similar to `row_winner`, this function checks if there is a winner in any column. It returns `True` if any column contains the same symbols (either 1 or 2).

### `diagonal_winner(board)`

`diagonal_winner` checks for a winner in both the main and secondary diagonals. If any diagonal contains the same symbols (either 1 or 2), it returns `True`.

### `game(board, n)`

The `game` function is the main game loop. It allows the user and CPU to take turns and keeps track of the game state. It continues until there is a winner or a draw.

## Usage

To play the game, you can run the script in Python. You will be prompted to make moves by entering row and column numbers. The game will display the board after each move and announce the winner or a draw when the game ends.

Example:
```bash
python tic_tac_toe.py

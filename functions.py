import numpy as np
import sys

# Function for the user's turn, where they input their move
def user_turn(board):
    row_position = int(input("Enter the row number: "))
    column_position = int(input("Enter the column number: "))
    board[row_position, column_position] = 1     

# Function for the CPU's turn to make a move
def cpu_turn(board, n):
    
    for row in range(n):

        # Check rows for potential winning moves
        if (np.count_nonzero(board[row] == 2) == n-1 or np.count_nonzero(board[row] == 1) == n-1) and 0 in board[row]:
            index = np.where(board[row] == 0)[0][0]
            board[row, index] = 2
            return
        
        column_values = board[:, row]

        # Check columns for potential winning moves
        if (np.count_nonzero(column_values == 2) == n-1 or np.count_nonzero(column_values == 1) == n-1) and 0 in column_values:
            column_values[column_values == 0] = 2
            board[:,row] = column_values
            return

        # Check main diagonal for potential winning moves
        if (np.count_nonzero(np.diag(board) == 2) == n-1 or np.count_nonzero(np.diag(board) == 1) == n-1) and 0 in np.diag(board):
            main_diag = np.array([2 if value == 0 else value for value in np.diag(board)])
            np.fill_diagonal(board,main_diag)
            return 

        anti_diagonal = np.diag(np.fliplr(board))

        # Check anti-diagonal for potential winning moves
        if (np.count_nonzero(anti_diagonal == 2) == n-1 or np.count_nonzero(anti_diagonal == 1) == n-1) and 0 in anti_diagonal:
            anti_diagonal = np.array([2 if value == 0 else value for value in anti_diagonal])
            np.fill_diagonal(np.fliplr(board),anti_diagonal)
            return

    # If no winning move is found, make a random move
    fila_aleatoria = np.random.randint(0, n)
    columna_aleatoria = np.random.randint(0, n)
        
    while board[fila_aleatoria, columna_aleatoria] != 0:
        fila_aleatoria = np.random.randint(0, n)
        columna_aleatoria = np.random.randint(0, n)

        if 0 not in board:
            print("Draw")
            sys.exit()
        
    board[fila_aleatoria, columna_aleatoria] = 2

# Function to check if there is a winner in a row
def row_winner(board):
    for row in board:
        if all(cell == 1 for cell in row) or all(cell == 2 for cell in row):
            return True

# Function to check if there is a winner in a column
def column_winner(board, n):
    for column in range(n):
        column_values = board[:, column]
        if all(cell == 1 for cell in column_values) or all(cell == 2 for cell in column_values):
            return True

# Function to check if there is a winner in a diagonal
def diagonal_winner(board):

    anti_diagonal = np.diag(np.fliplr(board))

    if all(cell == 1 for cell in np.diag(board)) or all(cell == 2 for cell in np.diag(board)) or all(cell == 1 for cell in anti_diagonal) or all(cell == 2 for cell in anti_diagonal):
        return True

# Function to run the game
def game(board, n):
    while 0 in board:
        print("User's Turn")
        user_turn(board)
        print(board)
        if row_winner(board) or column_winner(board, n) or diagonal_winner(board):
            print("We have a winner")
            break
        cpu_turn(board, n)
        print("CPU's Turn")
        print(board)
        if row_winner(board) or column_winner(board, n) or diagonal_winner(board):
            print("We have a winner")
            break
import numpy as np
import sys

def user_turn(board):
    row_position = int(input("Enter the row number: "))
    column_position = int(input("Enter the column number: "))
    board[row_position, column_position] = 1     

def cpu_turn(board, n):
    
    for row in range(n):
        if (np.count_nonzero(board[row] == 2) == n-1 or np.count_nonzero(board[row] == 1) == n-1) and 0 in board[row]:
            index = np.where(board[row] == 0)[0][0]
            board[row, index] = 2
            return
        
        column_values = board[:, row]
    
        if (np.count_nonzero(column_values == 2) == n-1 or np.count_nonzero(column_values == 1) == n-1) and 0 in column_values:
            column_values[column_values == 0] = 2
            board[:,row] = column_values
            return

        if (np.count_nonzero(np.diag(board) == 2) == n-1 or np.count_nonzero(np.diag(board) == 1) == n-1) and 0 in np.diag(board):
            main_diag = np.array([2 if value == 0 else value for value in np.diag(board)])
            np.fill_diagonal(board,main_diag)
            return 

        anti_diagonal = np.diag(np.fliplr(board))

        if (np.count_nonzero(anti_diagonal == 2) == n-1 or np.count_nonzero(anti_diagonal == 1) == n-1) and 0 in anti_diagonal:
            anti_diagonal = np.array([2 if value == 0 else value for value in anti_diagonal])
            np.fill_diagonal(np.fliplr(board),anti_diagonal)
            return

    fila_aleatoria = np.random.randint(0, n)
    columna_aleatoria = np.random.randint(0, n)
        
    while board[fila_aleatoria, columna_aleatoria] != 0:
        fila_aleatoria = np.random.randint(0, n)
        columna_aleatoria = np.random.randint(0, n)

        if 0 not in board:
            print("Draw")
            sys.exit()
        
    board[fila_aleatoria, columna_aleatoria] = 2

def row_winner(board):
    for row in board:
        if all(cell == 1 for cell in row) or all(cell == 2 for cell in row):
            return True

def column_winner(board, n):
    for column in range(n):
        column_values = board[:, column]
        if all(cell == 1 for cell in column_values) or all(cell == 2 for cell in column_values):
            return True

def diagonal_winner(board, n):
    counter = 0
    diag = []

    for row in range(n):
        diag.append(board[counter][-(counter+1)])
        counter += 1

    if all(cell == 1 for cell in np.diag(board)) or all(cell == 2 for cell in np.diag(board)) or all(cell == 1 for cell in diag) or all(cell == 2 for cell in diag):
        return True

def game(board, n):
    while 0 in board:
        print("User's Turn")
        user_turn(board)
        print(board)
        if row_winner(board) or column_winner(board, n) or diagonal_winner(board,n):
            print("We have a winner")
            break
        cpu_turn(board, n)
        print("CPU's Turn")
        print(board)
        if row_winner(board) or column_winner(board, n) or diagonal_winner(board,n):
            print("We have a winner")
            break
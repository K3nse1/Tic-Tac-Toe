import numpy as np

def user_turn(board):
    row_position = int(input("Enter the row number: "))
    column_position = int(input("Enter the column number: "))
    board[row_position, column_position] = 1     

def cpu_turn(board, n):

    for row in range(n):
        if np.count_nonzero(board[row] == 1) == 2 and 0 in board[row]:
            index = np.where(board[row] == 0)[0][0]
            board[row, index] = 2
            return

    fila_aleatoria = np.random.randint(0, n)
    columna_aleatoria = np.random.randint(0, n)
        
    while board[fila_aleatoria, columna_aleatoria] != 0:
        fila_aleatoria = np.random.randint(0, n)
        columna_aleatoria = np.random.randint(0, n)

        if 0 not in board:
            print("Draw")
            break
        
    board[fila_aleatoria, columna_aleatoria] = 2

# def cpu_turn(board, n):

    
#     random_row = np.random.randint(0, n)
#     random_column = np.random.randint(0, n)
    
#     while board[random_row, random_column] != 0:
#         random_row = np.random.randint(0, n)
#         random_column = np.random.randint(0, n)
#         if 0 not in board:
#             print("Draw")
#             break
            
    # board[random_row, random_column] = 2

def row_winner(board):
    for row in board:
        if all(cell == 1 for cell in row) or all(cell == 2 for cell in row):
            return True

def column_winner(board, n):
    for column in range(n):
        column_values = board[:, column]
        if all(cell == 1 for cell in column_values) or all(cell == 2 for cell in column_values):
            return True

def diagonal_winner(board):
    counter = 0
    diag = []

    for row in range(len(board)):
        diag.append(board[counter][-(counter+1)])
        counter += 1

    if all(cell == 1 for cell in np.diag(board)) or all(cell == 2 for cell in np.diag(board)) or all(cell == 1 for cell in diag) or all(cell == 2 for cell in diag):
        return True

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

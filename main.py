import numpy as np
from functions import * # Import user-defined functions from the 'functions' module

# Prompt the user to enter the number of rows for the game board
n = int (input ("Enter the number of rows that the board will have: "))

# Ensure that the entered number is greater than 2; keep asking until a valid number is provided
while n <= 2:
    n = int (input ("The number must be greater than two. Please enter another one:"))
        
# Create an empty game board with dimensions n x n
board = np.zeros (shape=(n,n))

# Display the initial state of the game board
print (board)

# Start the game by calling the 'game' function with the created board and the specified board size 'n'
game (board, n)
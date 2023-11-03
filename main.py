import numpy as np
from funciones import *

n = int (input ("Enter the number of rows that the board will have: "))

while n <= 2:
    n = int (input ("The number must be greater than two. Please enter another one:"))
        
board = np.zeros (shape=(n,n))
print (board)

game (board, n)
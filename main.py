import numpy as np

n = int (input ("Introduce el tamaño del tablero: 3x3, 4x4..."))

def determinar_ganador(tablero):

    for row in tablero:
        if all(cell == 1 for cell in row) or all(cell == 2 for cell in row):
            return True

    for column in range(n):
        column = tablero[:, column]
        if all (cell == 1 for cell in column) or all(cell == 2 for cell in column):
            return True

tablero = np.zeros (shape=(n,n))
print (tablero)

while 0 in tablero:
    
    print ("Turno del usuario")
    posicion_fila =  int ((input ("Introduce el número de fila: ")))
    posicion_columna = int ((input ("Introduce el número de columna: ")))
    tablero [posicion_fila, posicion_columna] = 1
    print (tablero)
    if determinar_ganador(tablero) == True:
        print ("Tenemos un ganador")
        break

    fila_aleatoria = np.random.randint (0,n)
    columna_aleatoria = np.random.randint (0,n)
    
    while tablero[fila_aleatoria, columna_aleatoria] != 0:
        fila_aleatoria = np.random.randint (0,n)
        columna_aleatoria = np.random.randint (0,n)
        if 0 not in tablero:
            print ("Empate")
            break
        
    tablero [fila_aleatoria, columna_aleatoria] = 2
    print ("Turno de la CPU")
    print (tablero)
    if determinar_ganador(tablero) == True:
        print ("Tenemos un ganador")
        break
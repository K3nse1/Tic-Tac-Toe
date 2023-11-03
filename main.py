import numpy as np

n = int (input ("Introduce el número de filas que tendrá el tablero: "))

def determinar_ganador(tablero):

    counter = 0
    diag = []

    for row in tablero:
        diag.append(tablero[counter][-(counter+1)])
        if all(cell == 1 or cell == 2 for cell in row) or all (cell == 1 or cell == 2 for cell in diag):
            return True
        counter += 1

    for column in range(n):
        column = tablero[:, column]
        if all (cell == 1 or cell == 2 for cell in column):
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
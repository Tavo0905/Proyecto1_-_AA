############################################
# Algoritmo de Backtracking                #
# Analisis de Algoritmos - Proyecto 1      #
# Gustavo Pérez / Mauricio Aguero          #
# 13/09/2021                               #
############################################
# Se van a ir probando distintos caminos   #
# hasta encontrar uno en el que no se      #
# repitan las fichas y se encuentren todas.#
############################################

############## IMPORTAR FUNCIONES ################

import dominoes as dom

############## FUNCIONES PRINCIPALES #####################

def getFicha(matriz, x,  y, ori, posiciones):
    try:
        if ori == "H":
            if [x, y] not in posiciones and [x, y+1] not in posiciones:
                return [matriz[x][y], matriz[x][y+1]]
        else:
            if [x, y] not in posiciones and [x+1, y] not in posiciones:
                return [matriz[x][y], matriz[x+1][y]]
    except:
        return False
    return False

def siguientePosicion(matriz, x, y, maxX, maxY, posiciones):
    while [x, y] in posiciones:
        y += 1
        if y >= maxY:
            x += 1
            y = 0
        if x >= maxX:
            return -1, -1
    return x, y

def devolverse(matriz, fichas, solucion, posiciones):
<<<<<<< Updated upstream
    while True:
        sol = solucion[-1]
        solucion = solucion[:-1]
        fichas = fichas[:-1]
        posiciones[:-2]

        if sol[2] == "H":
            ficha = getFicha(matriz, sol[0], sol[1], "V", posiciones)
            if ficha != False:
                solucion.append([sol[0], sol[1], "V"])
                fichas.append(ficha)
                posiciones.append([sol[0], sol[1]])
=======
    print("DEVOLVERSE")
    while True:
        print(solucion)
        sol = solucion[-1]
        solucion = solucion[:-1]
        fichas = fichas[:-1]
        posiciones = posiciones[:-2]

        if sol[2] == "H":
            print("H")
            ficha = getFicha(matriz, sol[0], sol[1], "V", posiciones)
            if ficha != False:
                print("not False")
                solucion.append([sol[0], sol[1], "V"])
                fichas.append(ficha)
                posiciones.append([sol[0], sol[1]])
                posiciones.append([sol[0]+1, sol[1]])
                print()
>>>>>>> Stashed changes
                return sol[0], sol[1], fichas, solucion, posiciones

def duplicas(fichas):
    encontradas = []
<<<<<<< Updated upstream
    
    for i in range(len(fichas)):
        print("fichas")
        print(fichas)
        print()
        ficha = fichas[i]
        if [ficha[0], ficha[1]] in encontradas or [ficha[1], ficha[0]] in encontradas:
            return True
=======
    print("fichas")
    print(fichas)
    print()
    
    for i in range(len(fichas)):
        ficha = fichas[i]
        if [ficha[0], ficha[1]] in encontradas or [ficha[1], ficha[0]] in encontradas:
            print("TRUE")
            return True
        encontradas.append(ficha)
>>>>>>> Stashed changes
    
    return False


<<<<<<< Updated upstream
def backtracking(matriz):
=======
def backtracking(n):
    matriz = False
    while (matriz == False):
        matriz = dom.create_puzzle(n)
    matriz = [[3, 0, 3, 1, 0], [2, 0, 3, 1, 1], [3, 1, 3, 2, 0], [0, 2, 2, 2, 1]]
>>>>>>> Stashed changes
    #Va probando como si todas las fichas fueran horizontales hasta que se encuentre una ficha duplicada
    #Se va devolviendo cuando hay una duplica
    fichasEncontradas = [] # [[1, 2], [2, 0], [3, 4], ...]
    solucion = []          # [[0, 0, H], [0, 2, V], [0, 3, V], ...]
    posiciones = []        # [[0, 0], [0, 1], [0, 2], [1, 2], ...]
    x = 0
    y = 0
    maxFilas = len(matriz)
    maxColumnas = len(matriz[0])
    while (True):
        x, y = siguientePosicion(matriz, x, y, maxFilas, maxColumnas, posiciones)
        if x == -1 or y == -1:
            break
        ori = "H"
        
        ficha = getFicha(matriz, x, y, ori, posiciones)

        rollback = False
        if ficha == False: #Ficha fuera de rango o repite una posicion
            ori = "V"
            ficha = getFicha(matriz, x, y, ori, posiciones)
            if ficha == False:
                x, y, fichasEncontradas, solucion, posiciones = devolverse(matriz, fichasEncontradas, solucion, posiciones)
                rollback = True

        if not rollback:
            fichasEncontradas.append(ficha)
            solucion.append([x, y, ori])
            posiciones.append([x, y])
            if ori == "H":
                posiciones.append([x, y+1])
            else:
                posiciones.append([x+1, y])
            if duplicas(fichasEncontradas):
                x, y, fichasEncontradas, solucion, posiciones = devolverse(matriz, fichasEncontradas, solucion, posiciones)
    print(matriz)
    print()
    print(solucion)

<<<<<<< Updated upstream
backtracking(dom.create_puzzle(3))
=======
backtracking(3)
>>>>>>> Stashed changes

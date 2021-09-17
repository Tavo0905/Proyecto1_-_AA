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

def getFicha(x,  y, ori):
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

def siguientePosicion(x, y):
    while [x, y] in posiciones:
        y += 1
        if y >= maxColumnas:
            x += 1
            y = 0
        if x >= maxFilas:
            return -1, -1
    return x, y

def insertarFicha(x, y, ori, ficha):
    solucion.append([x, y, ori])
    fichasEncontradas.append(ficha)
    posiciones.append([x, y])
    if ori == "H":
        posiciones.append([x, y+1])
    else:
        posiciones.append([x+1, y])


def devolverse():
    global solucion
    global fichasEncontradas
    global posiciones
    
    while True:
        sol = solucion[-1]
        solucion = solucion[:-1]
        fichasEncontradas = fichasEncontradas[:-1]
        posiciones = posiciones[:-2]

        if sol[2] == "H":
            ficha = getFicha(sol[0], sol[1], "V")
            if ficha != False:
                insertarFicha(sol[0], sol[1], "V", ficha)
                return sol[0], sol[1]

def duplicas():
    encontradas = []
    
    for i in range(len(fichasEncontradas)):
        ficha = fichasEncontradas[i]
        if [ficha[0], ficha[1]] in encontradas or [ficha[1], ficha[0]] in encontradas:
            return True
        encontradas.append(ficha)
    
    return False

def imprimirSolucion(matriz, solucion):
    posiciones.clear()
    solucionFinal = []
    for sol in solucion:
        ficha = getFicha(sol[0], sol[1], sol[2])
        ficha.append(sol[2])
        solucionFinal.append(ficha)

    for fila in matriz:
        print(fila)

    print()
    print(solucionFinal)


def backtracking(n):
    global matriz
    matriz = False
    while (matriz == False):
        matriz = dom.create_puzzle(n)

    #Va probando como si todas las fichas fueran horizontales hasta que se encuentre una ficha duplicada
    #Se va devolviendo cuando hay una duplica

    global fichasEncontradas
    fichasEncontradas = [] # [[1, 2], [2, 0], [3, 4], ...]
    global solucion
    solucion = []          # [[0, 0, H], [0, 2, V], [0, 3, V], ...]
    global posiciones
    posiciones = []        # [[0, 0], [0, 1], [0, 2], [1, 2], ...]

    x = 0
    y = 0

    global maxFilas
    maxFilas = len(matriz)
    global maxColumnas
    maxColumnas = len(matriz[0])

    while (True):
        x, y = siguientePosicion(x, y)
        if x == -1 or y == -1:
            break

        ori = "H"
        ficha = getFicha(x, y, ori)

        rollback = False
        if ficha == False: #Ficha fuera de rango o repite una posicion
            ori = "V"
            ficha = getFicha(x, y, ori)
            if ficha == False:
                x, y = devolverse()
                rollback = True

        if not rollback:
            insertarFicha(x, y, ori, ficha)
            if duplicas():
                x, y = devolverse()
    
    imprimirSolucion(matriz, solucion)

backtracking(3)

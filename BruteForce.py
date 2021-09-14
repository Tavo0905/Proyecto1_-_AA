############################################
# Algoritmo de Fuerza Bruta                #
# Analisis de Algoritmos - Proyecto 1      #
# Gustavo Pérez / Mauricio Aguero          #
# 13/09/2021                               #
############################################
# Vamos a realizar todas las combinaciones #
# posibles para determinar cuales solucio- #
# nes son correctas y cuales no.           #
############################################

############## IMPORTAR FUNCIONES ################

import dominoes as dom

############## FUNCIONES PRINCIPALES #####################

def binario(n):
    # Convierte un numero natural en binario
    total = 0
    i = 0
    while (n > 0):
        total += (n % 2) * (10 ** i)
        n //= 2
        i += 1
    return total

def contador(num):
    # Cuenta la cantidad de digitos en un numero
    total = 0
    while (num > 0):
        total += 1
        num //= 10
    if (total == 0):
        return 1
    return total

def generarSolucion(total, n):
    # Genera una posible solucion a la matriz
    # Agrega ceros en caso de que el numero binario no
    # cuente con la cantidad exacta de soluciones
    bin = binario(n)
    solucion = "0" * (total - contador(bin)) + str(bin)
    return solucion

def comparador(matriz, numFichas, maxFilas, maxColumnas, solucion):
    # Compara la solucion dada con la matriz para ver si es posible
    fichas = []
    iSol = 0
    sigCol = maxColumnas
    sigFila = maxFilas
    for iFilas in range(maxFilas):
        for iColumnas in range(maxColumnas):
            if (matriz[iFilas][iColumnas] == "*"):      # En caso de que ya haya sido tomado en cuenta
                continue
            if solucion[iSol] == "0":                   # Si la solucion para esta ficha es horizontal
                if ((iColumnas + 1) == sigCol):         # Si la solucion propone que es horizontal, pero es el final de una fila
                    return fichas, False
                if (matriz[iFilas][iColumnas + 1] == "*"):  # Si la solucion propone que es horizontal, pero el siguiente numero
                    return fichas, False                    # ya fue tomado
                if ((matriz[iFilas][iColumnas], matriz[iFilas][iColumnas + 1]) in fichas) or\
                    ((matriz[iFilas][iColumnas + 1], matriz[iFilas][iColumnas]) in fichas): # Si ya está incluido en la solucion
                    return fichas, False
                else:                                       # Si la combinacion es valida
                    fichas.append((matriz[iFilas][iColumnas], matriz[iFilas][iColumnas + 1]))
                    matriz[iFilas][iColumnas] = matriz[iFilas][iColumnas + 1] = "*"     # Convierte las fichas en * para confirmar su uso
                    iSol += 1                               # Siguiente de la solucion
            elif solucion[iSol] == "1":                 # Si la solucion para esta ficha es vertical
                if ((iFilas + 1) == sigFila):           # Si la solucion propone que es vertical, pero es el final de la columna
                    return fichas, False
                if ((matriz[iFilas + 1][iColumnas], matriz[iFilas][iColumnas]) in fichas) or\
                    ((matriz[iFilas][iColumnas], matriz[iFilas + 1][iColumnas]) in fichas): # Si ya está incluido en la solucion
                    return fichas, False
                else:                                   # Si la combinacion es valida
                    fichas.append((matriz[iFilas][iColumnas], matriz[iFilas + 1][iColumnas]))
                    matriz[iFilas][iColumnas] = matriz[iFilas + 1][iColumnas] = "*"
                    iSol += 1
    return fichas, True                             # Retorna las fichas correctas y un true para validar

def adjuntarSolucion(fichas, solucion):
    # Agrega un formato para la solucion
    # Indica la ficha correspondiente y la orientacion
    solAdj = []
    orientacion = ""
    for indice in range(len(fichas)):
        if (solucion[indice] == "0"):       # Establece la orientacion
            orientacion = "H"
        else:
            orientacion = "V"
        solAdj.append((fichas[indice][0], fichas[indice][1], orientacion))
    if len(solAdj) < len(fichas):           # Validacion para evitar errores
        return False
    return solAdj

def copiadorMatriz(matriz):
    # Copia la matriz en una nueva
    repuesto = []
    for fila in matriz:
        repuesto.append(fila.copy())
    return repuesto


def bruteForce(matriz):
    # Algoritmo de soluciones
    # Crea todos los escenarios posibles y los evalua
    print(matriz)
    i = 0
    repuesto = copiadorMatriz(matriz)       # Crea un repuesto de la matriz
    maxFilas = len(matriz)
    maxColumnas = len(matriz[0])
    numFichas = (maxFilas * maxColumnas) // 2       # Determina la cantidad de fichas
    while (True):                                   # Encicla hasta que llegue al limite
        matriz = copiadorMatriz(repuesto)
        sol = generarSolucion(numFichas, i)         # Crea una posible solucion
        if (sol == ("1" * numFichas)):              # Ultimo caso posible     
            fichas, flag = comparador(matriz, numFichas, maxFilas, maxColumnas, sol) # Compara la solucion, ve si es valida
            if (flag == True):                      # En caso de que sea valida, imprime el formato
                print(adjuntarSolucion(fichas, sol))
            break
        else:
            fichas, flag = comparador(matriz, numFichas, maxFilas, maxColumnas, sol)    # Valida si la solucion es correcta
            if (flag == True):
                print(adjuntarSolucion(fichas, sol))
        i += 1
    return



bruteForce(dom.create_puzzle(3))
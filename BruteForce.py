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

############## CONVERSOR A BINARIO ##############

def binario(n):
    total = 0
    i = 0
    while (n > 0):
        total += (n % 2) * (10 ** i)
        n //= 2
        i += 1
    return total

def contador(num):
    total = 0
    while (num > 0):
        total += 1
        num //= 10
    if (total == 0):
        return 1
    return total

def generarSolucion(total, n):
    bin = binario(n)
    solucion = "0" * (total - contador(bin)) + str(bin)
    return solucion

def comparador(matriz, numFichas, maxFilas, maxColumnas, solucion):
    fichas = []
    iSol = 0
    sigCol = maxColumnas
    sigFila = maxFilas
    for iFilas in range(maxFilas):
        for iColumnas in range(maxColumnas):
            if (matriz[iFilas][iColumnas] == "*"):
                continue
            if solucion[iSol] == "0":
                if ((iColumnas + 1) == sigCol):
                    return fichas, False
                if (matriz[iFilas][iColumnas + 1] == "*"):
                    return fichas, False
                if ((matriz[iFilas][iColumnas], matriz[iFilas][iColumnas + 1]) in fichas) or\
                    ((matriz[iFilas][iColumnas + 1], matriz[iFilas][iColumnas]) in fichas):
                    return fichas, False
                else:
                    fichas.append((matriz[iFilas][iColumnas], matriz[iFilas][iColumnas + 1]))
                    matriz[iFilas][iColumnas] = matriz[iFilas][iColumnas + 1] = "*"
                    iSol += 1
            elif solucion[iSol] == "1":
                if ((iFilas + 1) == sigFila):
                    return fichas, False
                if ((matriz[iFilas + 1][iColumnas], matriz[iFilas][iColumnas]) in fichas) or\
                    ((matriz[iFilas][iColumnas], matriz[iFilas + 1][iColumnas]) in fichas):
                    return fichas, False
                else:
                    fichas.append((matriz[iFilas][iColumnas], matriz[iFilas + 1][iColumnas]))
                    matriz[iFilas][iColumnas] = matriz[iFilas + 1][iColumnas] = "*"
                    iSol += 1
    return fichas, True

def adjuntarSolucion(fichas, solucion):
    solAdj = []
    orientacion = ""
    for indice in range(len(fichas)):
        if (solucion[indice] == "0"):
            orientacion = "H"
        else:
            orientacion = "V"
        solAdj.append((fichas[indice][0], fichas[indice][1], orientacion))
    if len(solAdj) < len(fichas):
        return False
    return solAdj

def copiadorMatriz(matriz):
    repuesto = []
    for fila in matriz:
        repuesto.append(fila.copy())
    return repuesto


def bruteForce(matriz):
    print(matriz)
    repuesto = copiadorMatriz(matriz)
    maxFilas = len(matriz)
    maxColumnas = len(matriz[0])
    numFichas = (maxFilas * maxColumnas) // 2
    for i in range(999999999):
        matriz = copiadorMatriz(repuesto)
        sol = generarSolucion(numFichas, i)
        if (sol == ("1" * numFichas)):
            fichas, flag = comparador(matriz, numFichas, maxFilas, maxColumnas, sol)
            if (flag == True):
                print(adjuntarSolucion(fichas, sol))
            break
        else:
            fichas, flag = comparador(matriz, numFichas, maxFilas, maxColumnas, sol)
            if (flag == True):
                print(adjuntarSolucion(fichas, sol))
    return



bruteForce(dom.create_puzzle(2))
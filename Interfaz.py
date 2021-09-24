############################################
# Interfaz gráfica                         #
# Analisis de Algoritmos - Proyecto 1      #
# Gustavo Pérez / Mauricio Aguero          #
# 18/09/2021                               #
############################################
# Se va a realizar una interfaz para re-   #
# presentar los resultados de los analisis #
# de los algoritmos, donde se le da la so- #
# lucion a la matriz de fichas utilizando  #
# ambos métodos.                           #
############################################

################ IMPORTAR MODULOS #####################

from tkinter.constants import END, INSERT
from BruteForce import bruteForce
from Backtracking import backtracking
from dominoes import create_puzzle
from tkinter import messagebox as mb
import tkinter as tk
import threading, time

################ CLASES #####################

class hiloBruteForce(threading.Thread):
    """Esta clase corresponde al método de solución de fuerza bruta.
       Se crea una clase hilo con el fin de tener dos flijos del
       porgrama, y de esta manera la interfaz gráfica no sufre de
       las iteraciones causadas por la solucion de la matriz.
            Entradas:
                -Frame actual
                -Matriz
            Salidas:
                -Text Widget
                -Solucion de la matriz
                -Tiempo de ejecucion
    """
    def __init__(self, pantalla, matriz):
        self.solucionBox = tk.Text(pantalla, width = 57, height = 15)
        self.tiempoLabel = tk.Label(pantalla)
        self.matrizSol = matriz
        self.tiempo = 0
        self.soluciones = []
        self.solValidas = ""
        threading.Thread.__init__(self)
    
    def run (self):
        self.solucionBox.insert(INSERT, "Generando solucion, espere un momento...")
        self.solucionBox.place(x = 20, y = 350)
        self.tiempo, self.soluciones = bruteForce(self.matrizSol)       # Algoritmo puro de fuerza bruta
        self.tiempoLabel.config(text = self.tiempo)
        self.tiempoLabel.place(x = 355, y = 657)
        self.solucionBox.delete("1.0", "end")
    
        for solucion in self.soluciones:        # Despliega las soluciones
            if solucion[1] == True:             # En caso de que la solucion sea valida
                self.solValidas += str(solucion[0]) + "\n---------------------------------------------------------\n"
            self.solucionBox.insert(INSERT, self.solValidas + str(solucion[0]))
            time.sleep(0.005)
            self.solucionBox.delete("1.0", "end")
        self.solucionBox.insert(INSERT, self.solValidas + "FINAL DE SOLUCIONES")

class hiloBacktracking(threading.Thread):
    """Con el mismo objetivo del hilo de fuerza bruta, se realiza
       el de backtracking, así la interfaz no sufre problemas
            Entradas:
                -Frame actual
                -Matriz
            Salidas:
                -Text Widget
                -Solucion de la matriz
                -Tiempo de ejecucion
    """
    def __init__(self, pantalla, matriz):
        self.solucionBox = tk.Text(pantalla, width = 57, height = 15)
        self.tiempoLabel = tk.Label(pantalla)
        self.matrizSol = matriz
        self.tiempo = 0
        self.soluciones = []
        self.solValidas = ""
        threading.Thread.__init__(self)
    
    def run (self):
        self.solucionBox.insert(INSERT, "Generando solucion, espere un momento...")
        self.solucionBox.place(x = 20, y = 350)
        self.tiempo, self.soluciones = backtracking(len(self.matrizSol) - 1)     # Algoritmo puro de backtracking
        self.tiempoLabel.config(text = self.tiempo)
        self.tiempoLabel.place(x = 355, y = 657)
        self.solucionBox.delete("1.0", "end")
        self.solucionBox.insert(INSERT, str(self.soluciones))
        self.solucionBox.insert(INSERT, "\n---------------------------------------------------------\n")
        self.solucionBox.insert(INSERT, "FINAL DE SOLUCIONES")


################ FUNCIONES ######################

def pruebaGUI(cantFichas, opcion):
    """Esta pantalla despliega las soluciones de los algoritmos,
       Despliega el método empleado, junto con la matriz generada
       y la solución que se va desplegando conforme itera dentro
       de las soluciones. Dependiendo de la opcion realiza el
       método elegido.
            Entradas:
                -Cantidad de fichas
                -Opción elegida
            Salidas:
                -Pantalla con las soluciones
    """
    try:                # En caso de que la entrada no sea un entero
        cantFichas = int(cantFichas)
        matriz = create_puzzle(cantFichas)
        if matriz != False:
            strMatriz = ""
            for linea in matriz:
                for num in linea:
                    strMatriz += str(num) + " "
                strMatriz += "\n"
        else:
            strMatriz = "False"
        
    
        pantalla = tk.Frame(ventana, width = 500, height = 700)
        pantalla.place(x = 0, y = 0)

        if opcion == 1:
            tituloP = tk.Label(pantalla, text = "Solución: Fuerza Bruta", font = ("Arial", 16))
            tituloP.place(x = 1, y = 1)
        else:
            tituloP = tk.Label(pantalla, text = "Solución: Backtracking", font = ("Arial", 16))
            tituloP.place(x = 1, y = 1)

        matrizTxt = tk.Label(pantalla, text = "Matriz generada:", font = ("Arial", 16))
        matrizTxt.place(x = 10, y = 70)

        solucionTxt = tk.Label(pantalla, text = "Solucion:", font = ("Arial", 16))
        solucionTxt.place(x = 10, y = 320)

        tiempoTxt = tk.Label(pantalla, text = "Tiempo de ejecucion:", font = ("Arial", 12))
        tiempoTxt.place(x = 200, y = 655)

        volver = tk.Button(pantalla, width = 10, text = "Volver", font = ("Arial", 12), bg = "gray70", command = pantalla.destroy)
        volver.place(x = 10, y = 655)

        matrizBox = tk.Text(pantalla, width = 30, height = 15)
        matrizBox.insert(INSERT, strMatriz)
        matrizBox.place(x = 200, y = 70)

        if opcion == 1:
            hiloBruteForce(pantalla, matriz).start()
        else:
            hiloBacktracking(pantalla, matriz).start()

        pantalla.mainloop()
        return
    except:
        mb.showerror("ERROR", "La entrada ingresada no es un entero.")
        return


############### PROGRAMA PRINCIPAL ################

ventana = tk.Tk()
ventana.geometry("500x700")
ventana.title("Juego de dominoes")

titulo = tk.Label(ventana, text = "Juego de dominoes", font = ("Arial", 28))
titulo.pack()

cantFichasLabel = tk.Label(ventana, text = "Ingrese el mayor numero de la ficha:", font = ("Arial", 14))
cantFichasLabel.place(x = 10, y = 150)

metodoTxt = tk.Label(ventana, text = "Elija el metodo de solucion:", font = ("Arial", 14))
metodoTxt.place(x = 10, y = 250)

cantFichas = tk.Entry(ventana)
cantFichas.place(x = 350, y = 155)

botonBruteForce = tk.Button(ventana, text = "Fuerza Bruta", font = ("Arial", 16), bg = "gray70",\
    command = lambda: pruebaGUI(cantFichas.get(), 1))
botonBruteForce.place(x = 300, y = 250)

botonBacktracking = tk.Button(ventana, text = "Backtracking", font = ("Arial", 16), bg = "gray70",\
    command = lambda: pruebaGUI(cantFichas.get(), 2))
botonBacktracking.place(x = 300, y = 300)


ventana.resizable(False, False)
ventana.mainloop()
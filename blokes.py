import pygame
from Colores import colores
from blokes import *


class Colores:
    Azul = (15, 65, 220)
    Rojo = (230, 20, 20)
    Verde = (50, 230, 25)
    Cyan = (20, 205, 210)
    Morado = (165, 0, 250)
    Amarillo = (235, 235, 5)
    Blanco = (255, 255, 255)
    Purpura = (246, 51, 255)

    def seleccion_colores(self):
        return [self.Azul, self.Rojo, self.Verde, self.Cyan, self.Morado, self.Amarillo, self.Blanco, self.Purpura]

class lugar:
    def __init__(self, fila, columna):
        self.fila, self.columna = fila, columna

#Plantilla Bloque
class Bloques:
    def __init__(self, id): #Inicializar el objeto del bloque
        self.id = id #Seleccion de bloque
        self.celdas =  { 0: [lugar(0, 0)], 1: [lugar(0, 0)], 2: [lugar(0, 0)], 3: [lugar(0, 0)]  }
        self.cell_size = 40 
        self.desplazamiento_fila = 0
        self.desplazamiento_columna = 0
        self.rotacion = 0
        self.colores = colores.seleccion_colores()

    #Movimiento
    def mover(self, fila, columna):
        self.desplazamiento_fila += fila
        self.desplazamiento_columna += columna

    def obtener_posiciones_celdas(self):
        i = self.celdas[self.rotacion]
        celdas_desplazadas = []
        for Lugar in i:
            Lugar = lugar(Lugar.fila + self.desplazamiento_fila, Lugar.columna + self.desplazamiento_columna)
            celdas_desplazadas.append(Lugar)
        return celdas_desplazadas

    def rotar(self):
        self.rotacion += 1
        if self.rotacion == len(self.celdas):
            self.rotacion = 0

    def deshacer_rotacion(self):
        self.rotacion -= 1
        if self.rotacion == -1:
            self.rotacion = len(self.celdas) - 1

    def dibujar(self, pantalla, x, y):
        i = self.obtener_posiciones_celdas()
        for celda in i:
            rectangulo = pygame.Rect(x + celda.columna * self.cell_size, 
            y + celda.fila * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(pantalla, self.colores[self.id], rectangulo)


class bloque1(Bloques):
    def __init__(self):
        super().__init__(id=1)
        self.celdas = { 
            0: [lugar(j, k) for j, k in [(0, 2), (1, 0), (1, 1), (1, 2)]],
            1: [lugar(j, k) for j, k in [(0, 1), (1, 1), (2, 1), (2, 2)]],
            2: [lugar(j, k) for j, k in [(1, 0), (1, 1), (1, 2), (2, 0)]],
            3: [lugar(j, k) for j, k in	[(0, 0), (0, 1), (1, 1), (2, 1)]]}
        self.mover(0, 3)

class bloque2(Bloques):
    def __init__(self):
        super().__init__(id=2)
        self.celdas = {
            0: [lugar(j, k) for j, k in [(0, 0), (1, 0), (1, 1), (1, 2)]],
            1: [lugar(j, k) for j, k in [(0, 1), (0, 2), (1, 1), (2, 1)]],
            2: [lugar(j, k) for j, k in [(1, 0), (1, 1), (1, 2), (2, 2)]],
            3: [lugar(j, k) for j, k in [(0, 1), (1, 1), (2, 0), (2, 1)]]}
        self.mover(0, 3)

class bloque3(Bloques):
    def __init__(self):
        super().__init__(id=3)
        self.celdas = {
            0: [lugar(j, k) for j, k in [(0, 0), (1, 0), (2, 0), (3, 0)]],
            1: [lugar(j, k) for j, k in [(1, 0), (1, 1), (1, 2), (1, 3)]],
            2: [lugar(j, k) for j, k in [(0, 0), (1, 0), (2, 0), (3, 0)]],
            3: [lugar(j, k) for j, k in [(1, 0), (1, 1), (1, 2), (1, 3)]]}
        self.mover(0, 4)

class bloque4(Bloques):
    def __init__(self):
        super().__init__(id=4)
        self.celdas = {
            0: [lugar(j, k) for j, k in [(0, 1), (0, 2), (1, 0), (1, 1)]],
            1: [lugar(j, k) for j, k in [(0, 1), (1, 1), (1, 2), (2, 2)]],
            2: [lugar(j, k) for j, k in [(1, 1), (1, 2), (2, 0), (2, 1)]],
            3: [lugar(j, k) for j, k in [(0, 0), (1, 0), (1, 1), (2, 1)]]}
        self.mover(0, 3)

class bloque5(Bloques):
    def __init__(self):
        super().__init__(id=5)
        self.celdas = {
            0: [lugar(j, k) for j, k in [(0, 0), (1, 0), (0, 1), (1, 1)]],
            1: [lugar(j, k) for j, k in [(0, 0), (1, 0), (0, 1), (1, 1)]],
            2: [lugar(j, k) for j, k in [(0, 0), (1, 0), (0, 1), (1, 1)]],
            3: [lugar(j, k) for j, k in [(0, 0), (1, 0), (0, 1), (1, 1)]]}
        self.mover(0, 4)

class bloque6(Bloques):
    def __init__(self):
        super().__init__(id=6)
        self.celdas = {
            0: [lugar(j, k) for j, k in [(0, 1), (1, 0), (1, 1), (1, 2)]],
            1: [lugar(j, k) for j, k in [(0, 1), (1, 1), (1, 2), (2, 1)]],
            2: [lugar(j, k) for j, k in [(1, 0), (1, 1), (1, 2), (2, 1)]],
            3: [lugar(j, k) for j, k in [(0, 1), (1, 0), (1, 1), (2, 1)]]}
        self.mover(0, 3)

class bloque7(Bloques):
	def __init__(self):
		super().__init__(id = 7)
		self.celdas = {
            0: [lugar(j, k) for j, k in [(0, 0), (0, 1), (1, 1), (1, 2)]],
            1: [lugar(j, k) for j, k in [(0, 2), (1, 1), (1, 2), (2, 1)]],
            2: [lugar(j, k) for j, k in [(1, 0), (1, 1), (2, 1), (2, 2)]],
            3: [lugar(j, k) for j, k in [(0, 1), (1, 0), (1, 1), (2, 0)]]}
		self.mover(0, 3)




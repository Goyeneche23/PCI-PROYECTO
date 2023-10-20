from tablero import Tablero
from blokes import *
import random
import pygame

class Juego:
    def __init__(self):
        self.tab = Tablero()
        self.bloques = [bloque1(), bloque2(), bloque3(), bloque4(), bloque5(), bloque6(), bloque7()]
        self.bloque_actual = self.obtener_bloque_aleatorio()
        self.siguiente_bloque = self.obtener_bloque_aleatorio()
        self.game_over = False

    def obtener_bloque_aleatorio(self):
        if not self.bloques:
            self.bloques = [bloque1(), bloque2(), bloque3(), bloque4(), bloque5(), bloque6(), bloque7()]
        bloque = random.choice(self.bloques)
        self.bloques.remove(bloque)
        return bloque

    def mover_izquierda(self):
        self.mover(0, -1)

    def mover_derecha(self):
        self.mover(0, 1)

    def mover_abajo(self):
        self.mover(1, 0)

    def mover(self, fila, columna):
        self.bloque_actual.mover(fila, columna)
        if not self.bloque_dentro() or not self.bloque_encaja():
            self.bloque_actual.mover(-fila, -columna)
            if fila == 1:
                self.bloquear_bloque()

    def bloquear_bloque(self):
        celdas = self.bloque_actual.obtener_posiciones_celdas()
        for posicion in celdas:
            self.tab.tab[posicion.fila][posicion.columna] = self.bloque_actual.id
        self.bloque_actual = self.obtener_bloque_aleatorio()
        self.siguiente_bloque = self.obtener_bloque_aleatorio()
        lineas_limpiadas = self.tab.fila_completa()
        if not self.bloque_encaja():
            self.game_over = True

    def reiniciar(self):
        self.tab.reiniciar()
        self.bloques = [bloque1(), bloque2(), bloque3(), bloque4(), bloque5(), bloque6(), bloque7()]
        self.bloque_actual = self.obtener_bloque_aleatorio()
        self.siguiente_bloque = self.obtener_bloque_aleatorio()

    def bloque_encaja(self):
        celdas = self.bloque_actual.obtener_posiciones_celdas()
        for celda in celdas:
            if not self.tab.libre(celda.fila, celda.columna):
                return False
        return True

    def rotar(self):
        self.bloque_actual.rotar()
        if not self.bloque_dentro() or not self.bloque_encaja():
            self.bloque_actual.deshacer_rotacion()

    def bloque_dentro(self):
        celdas = self.bloque_actual.obtener_posiciones_celdas()
        for celda in celdas:
            if not self.tab.dentro(celda.fila, celda.columna):
                return False
        return True

    def imprimir_bloques(self, pantalla):
        self.tab.dibujar(pantalla)
        self.bloque_actual.dibujar(pantalla, 0, 0)
        self.siguiente_bloque.dibujar(pantalla, 350, 365)


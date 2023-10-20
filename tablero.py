
import pygame, sys
from blokes import *

class Tablero:
    def __init__(self): #Inicializar Tablero
        self.cell_size = 40 #Tamaño Celdas
        self.num_filas = 20 
        self.num_columnas = 10
        self.colores = self.seleccion_colores()
        self.tab = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    # Print self.tab
    def imprimir_celdas(self):
        for fila in self.tab:
            for celda in fila:
                print(celda, end=" ")
            print() 

    # Dar Colores
    def seleccion_colores(self):
        Gris = (25, 30, 40)
        Azul = (15, 65, 220)
        Azuloscuro = (45, 45, 127) 
        Rojo = (230, 20, 20)
        Verde = (50, 230, 25)
        Cyan = (20, 205, 210)
        Morado = (165, 0, 250)
        Amarillo = (235, 235, 5)
        Blanco = (255, 255, 255)

        return [Gris, Azul, Azuloscuro, Rojo, Verde, Cyan, Morado, Amarillo, Blanco]

    #Dibujar contornos (limites)
    def celdas(self, pantalla):
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                valor_celda = self.tab[fila][columna]
                x = columna * self.tamaño_celda + 1
                y = fila * self.tamaño_celda + 1
                horizontal = self.tamaño_celda - 1
                vertical = self.tamaño_celda - 1
                rectangulo = pygame.Rect(x, y, horizontal, vertical)
                pygame.draw.rect(pantalla, self.colores[valor_celda], rectangulo)

    #Decoracion Lado derecho
    def contorno(pantalla):
        neon1 = (34, 234, 69)
        neon2 = (15, 192, 57)
        neon3 = (28, 150, 41)
        neon4 = (1, 82, 40)
        neon5 = (0, 0, 0)
        #Horizontal 1
        pygame.draw.line(pantalla, neon5, (401, 1), (650, 1), 5)
        pygame.draw.line(pantalla, neon4, (401, 6), (645, 6), 5)
        pygame.draw.line(pantalla, neon3, (401, 11), (640, 11), 5)
        pygame.draw.line(pantalla, neon2, (401, 16), (635, 16), 5)
        pygame.draw.line(pantalla, neon1, (401, 21), (630, 21), 5)
        #Vertical
        pygame.draw.line(pantalla, neon5, (650, 0), (650, 800), 5)
        pygame.draw.line(pantalla, neon4, (645, 4), (645, 797), 5)
        pygame.draw.line(pantalla, neon3, (640, 9), (640, 792), 5)
        pygame.draw.line(pantalla, neon2, (635, 14), (635, 787), 5)
        pygame.draw.line(pantalla, neon1, (630, 19), (630, 782), 5)
        #Horizontal 2
        pygame.draw.line(pantalla, neon5, (650, 800), (403, 800), 5)
        pygame.draw.line(pantalla, neon4, (645, 795), (403, 795), 5)
        pygame.draw.line(pantalla, neon3, (640, 790), (403, 790), 5)
        pygame.draw.line(pantalla, neon2, (635, 785), (403, 785), 5)
        pygame.draw.line(pantalla, neon1, (630, 780), (403, 780), 5)     
        #Vertical 2   
        pygame.draw.line(pantalla, neon5, (403, 800), (403, 1), 5)
        pygame.draw.line(pantalla, neon4, (408, 795), (408, 6), 5)
        pygame.draw.line(pantalla, neon3, (413, 790), (413, 11), 5)
        pygame.draw.line(pantalla, neon2, (418, 785), (418, 16), 5)
        pygame.draw.line(pantalla, neon1, (423, 780), (423, 21), 5)    
        #v
        pygame.draw.line(pantalla, neon1, (3, 1), (400, 1), 3)    
        #h
        pygame.draw.line(pantalla, neon1, (3, 0), (3, 835), 3)    

    #Decoracion Contorno titulo
    def cuadro_titulo(pantalla):
        # Colores
        neon1 = (34, 234, 69)
        neon2 = (15, 192, 57)
        neon3 = (28, 150, 41)
        neon4 = (1, 82, 40)
        negro = (0, 0, 0)
        # Definir las coordenadas y dimensiones del cuadro del título
        x, y, ancho, alto = 450, 80, 151.2, 100
        # Dibuja el relleno del cuadro con el color de fondo (negro)
        pygame.draw.rect(pantalla, negro, (x, y, ancho, alto), 0)
        # Dibuja el contorno con el degradado de colores
        pygame.draw.rect(pantalla, neon1, (x, y, ancho, alto), 3)
        pygame.draw.rect(pantalla, neon2, (x - 3, y - 3, ancho + 6, alto + 6), 3)
        pygame.draw.rect(pantalla, neon3, (x - 6, y - 6, ancho + 12, alto + 12), 3)
        pygame.draw.rect(pantalla, neon4, (x - 9, y - 9, ancho + 18, alto + 18), 3)
        pygame.draw.rect(pantalla, negro, (x - 12, y - 12, ancho + 24, alto + 24), 3)
               
    #Contorno           
    def dibujar(self, pantalla):
        for fila in range(len(self.tab)):
            for columna in range(len(self.tab[0])):
                cell_value = self.tab[fila][columna]
                cell_x = columna * self.cell_size 
                cell_y = fila * self.cell_size
                cell_rect = pygame.Rect(cell_x, cell_y, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(pantalla, self.colores[cell_value], cell_rect)


    def dentro(self, fila, columna):
        return 0 <= fila < self.num_filas and 0 <= columna < self.num_columnas

    def libre(self, fila, columna):
        return self.tab[fila][columna] == 0

    def fila_completa(self):
        completadas = 0
        for fila in range(self.num_filas - 1, 0, -1):
            if all(self.tab[fila]):
                self.eliminar_fila(fila)
                completadas += 1
            elif completadas > 0:
                self.bajar(fila, completadas)
        return completadas

    def eliminar_fila(self, fila):
        for columna in range(self.num_columnas):
            self.tab[fila][columna] = 0

    def bajar(self, fila, num_filas):
        for columna in range(self.num_columnas):
            self.tab[fila + num_filas][columna] = self.tab[fila][columna]
            self.tab[fila][columna] = 0

    def reiniciar(self):
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                self.tab[fila][columna] = 0

    def dibujar_cuadro_contorno(pantalla, x, y):
        negro = (0, 0, 0)
        verde = (0, 255, 0)
        horizontal = 185
        vertical = 135
        cuerpo = 5
        pygame.draw.rect(pantalla, negro, (x, y, horizontal, vertical), cuerpo)
        pygame.draw.line(pantalla, verde, (x, y + vertical // 2), (x + horizontal, y + vertical // 2), cuerpo)



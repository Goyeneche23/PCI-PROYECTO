import pygame, sys
import matplotlib.pyplot as plt
import colorsys

class Tablero:
    def __init__(self):
        self.numFilas = 20
        self.numColumnas = 10
        self.cell_size = 40
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
        self.colores = self.seleccion_colores()

    def print_tab(self):
        for fila in self.tab:
            print(" ".join(map(str, fila)))

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

    def celdas(self, pantalla):
        for fila in range(self.numFilas):
            for columna in range(self.numColumnas):
                cell_value = self.tab[fila][columna]
                cell_rect = pygame.Rect(columna*self.cell_size +1, fila*self.cell_size +1, self.cell_size -1, self.cell_size -1)
                Verde = (50, 230, 25)
                pygame.draw.rect(pantalla, Verde[cell_value], cell_rect)

    def contorno(self, pantalla):
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

    def cuadro_titulo(self, pantalla):
        negro = (0, 0, 0)
        pygame.draw.rect(pantalla, negro, (450,80,151.2,100), 10)

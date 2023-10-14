# Tetris Python 0.0
# Fecha: 20-09-2023
#Version pygame-ce 2.3.1 (SDL 2.26.5, Python 3.11.1)
#Modulos
#estoy teniendo problemas para imprimir los bloques (piezas) en el tablero.
import pygame, sys
from tablero import Tablero
from bloques import *
from blokes import *

pygame.init()
Cyan = (20, 205, 210) #tupla RGB
Neon = (57, 255, 40) #tupla RGB
#Pantalla
pantalla = pygame.display.set_mode((652.00, 835.00))
#Titulo
pygame.display.set_caption("Tetris, By Juan Jose")

temporizador = pygame.time.Clock()

pygame.font.get_fonts()
pantalla.fill(Neon)

game_tab = Tablero()
game_tab.print_tab()
block = bloque1()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    block.draw(pantalla)
    game_tab.tab[5][1] = 3

    game_tab.celdas(pantalla)
    game_tab.contorno(pantalla)
    game_tab.cuadro_titulo(pantalla)

    pygame.display.update()
    temporizador.tick(50)


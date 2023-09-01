# Tetris Game, written in Python
# Date: 01-09-2023

import pygame, sys
from tablero import Tablero

pygame.init()
Azul_fondo = (45, 45, 127)

pantalla = pygame.display.set_mode((350.00, 700.00))
pygame.display.set_caption("Tetris")

temporizador = pygame.time.Clock()

game_tab = Tablero()
game_tab.print_tab()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(Azul_fondo)
    pygame.display.update()
    temporizador.tick(50)

# Tetris Python 0.0
# Fecha: 20-09-2023

#Modulos
import pygame, sys
from tablero import Tablero
import matplotlib.pyplot as plt 
import colorsys

pygame.init()
Cyan = (20, 205, 210) #tupla RGB
Neon = (57, 255, 40) #tupla RGB

#Pantalla
pantalla = pygame.display.set_mode((652.00, 835.00))
#Titulo
pygame.display.set_caption("Tetris, By Juan Jose")

temporizador = pygame.time.Clock()

game_tab = Tablero()
game_tab.print_tab()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(Neon)
    
    game_tab.celdas(pantalla)
    game_tab.contorno(pantalla)
    game_tab.cuadro_titulo(pantalla)

    pygame.display.update()
    temporizador.tick(50)



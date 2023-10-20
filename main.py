# Tetris Python 1.0
# Fecha: 19-10-2023
#Version pygame-ce 2.3.1 (SDL 2.26.5, Python 3.11.1)

#Modulos
import pygame
from tablero import Tablero
from blokes import *
from Game import Juego

# Inicialización de Pygame
pygame.init()

#Colores para main
NEON = (57, 255, 40)  #RGB
NEGRO = (0, 0, 0)  #RGB

# Palabras Impresas
title_font = pygame.font.Font(None, 40)
game_over_surface = title_font.render("GAME OVER", True, NEON)
Title_tet = title_font.render("TETRIS", True, NEON)



# Creación de la pantalla
pantalla = pygame.display.set_mode((652, 835))
pantalla.fill(NEON)
#Nombre programa
pygame.display.set_caption("Tetris, por Juan José")

# Musica y Volumen
musica = pygame.mixer.music.load("MOONDOG Birds Lament.remix.wav")
perdiste = pygame.mixer.Sound("mixkit-arcade-retro-game-over-213.wav")
perdiste.set_volume(.15)
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play(-1)


temporizador = pygame.time.Clock()

# Tablero y decoracion (tablero.py)
game_tab = Tablero()
game_tab.imprimir_celdas()
Tablero.contorno(pantalla)
Tablero.cuadro_titulo(pantalla)
Tablero.dibujar_cuadro_contorno(pantalla, 435, 325)
pantalla.blit(Title_tet, (475, 120, 150, 100))


score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# Funcionalidad (Game.py)
game = Juego()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 250)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Controles
        keys = pygame.key.get_pressed()
        if not game.game_over:
            if keys[pygame.K_LEFT]:
                game.mover_izquierda()
            elif keys[pygame.K_RIGHT]:
                game.mover_derecha()
            elif keys[pygame.K_DOWN]:
                game.mover_abajo()
            elif keys[pygame.K_UP]:
                game.rotar()

        if event.type == GAME_UPDATE and not game.game_over:
            game.mover_abajo()

    # Condicionante Perdiste
    if game.game_over:
        pantalla.fill(NEGRO)
        pantalla.blit(game_over_surface, (450, 200, 120, 120))
        pygame.mixer.music.stop()
        perdiste.play()


    game.imprimir_bloques(pantalla)

    pygame.display.update()
    temporizador.tick(50)

pygame.quit()


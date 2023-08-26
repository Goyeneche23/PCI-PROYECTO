# Tetris Game, written in Python
# Date: 25-08-2023

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(50)

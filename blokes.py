import pygame
from Colores import colores

class Bloques:	
	def __init__(self, id):
		self.id = id
		self.cells = {}
		self.cell_size = 40
		self.rotacion = 0
		self.color = colores.seleccion_colores()

	def draw(self, pantalla):
		formas = self.cells[self.rotacion]
		for i in formas:
			forma_rect = pygame.Rect(tile.columna*self.cell_size +1, tile.fila*self.cell_size +1, self.cell_size -1, self.cell_size -1)
			pygame.draw.rect(pantalla, self.color[self.id], forma_rect)


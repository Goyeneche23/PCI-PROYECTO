import pygame
from Colores import colores

class lugar:
	def __init__(self, row, column):
		self.row = row
		self.column = column

class Bloques:
	def __init__(self, id):
		self.numero = id
		self.cells = {}
	    self.cell_size = 40
	    self.rotacion = 0
	    self.color = colores.seleccion_colores()

	def __init__(self, pantalla):


	class posicion:
		def __init__(self, fila, columna):
			self.fila = fila
			self.columna = columna

	class bloque1(Bloques):
		def __init__(self):
			super().__init__(id = 1)
			self.cells = {
				0: [lugar(0, 2), lugar(1, 0), lugar(1, 1), lugar(1, 2)],
				1: [lugar(0, 1), lugar(1, 1), lugar(2, 1), lugar(2, 2)],
				2: [lugar(1, 0), lugar(1, 1), lugar(1, 2), lugar(2, 0)],
				3: [lugar(0, 0), lugar(0, 1), lugar(1, 1), lugar(2, 1)]
			}

	class bloque2(Bloques):
		def __init__(self):
			super().__init__(id = 2)
			self.cells = {
				0: [lugar(0, 0), lugar(1, 0), lugar(1, 1), lugar(1, 2)],
            	1: [lugar(0, 1), lugar(0, 2), lugar(1, 1), lugar(2, 1)],
            	2: [lugar(1, 0), lugar(1, 1), lugar(1, 2), lugar(2, 2)],
            	3: [lugar(0, 1), lugar(1, 1), lugar(2, 0), lugar(2, 1)]
			}

	class bloque3(Bloques):
		def __init__(self):
			super().__init__(id = 3)
			self.cells = {
				0: [lugar(0, 0), lugar(1, 0), lugar(1, 1), lugar(1, 2)],
            	1: [lugar(0, 1), lugar(0, 2), lugar(1, 1), lugar(2, 1)],
            	2: [lugar(1, 0), lugar(1, 1), lugar(1, 2), lugar(2, 2)],
            	3: [lugar(0, 1), lugar(1, 1), lugar(2, 0), lugar(2, 1)]
			}

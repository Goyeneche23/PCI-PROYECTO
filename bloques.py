import pygame
from Colores import colores
from blokes import Bloques

class lugar:
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

class bloque4(Bloques):
		def __init__(self):
			super().__init__(id = 4)
			self.cells = {
            0: [lugar(0, 1), lugar(0, 2), lugar(1, 0), lugar(1, 1)],
            1: [lugar(0, 1), lugar(1, 1), lugar(1, 2), lugar(2, 2)],
            2: [lugar(1, 1), lugar(1, 2), lugar(2, 0), lugar(2, 1)],
            3: [lugar(0, 0), lugar(1, 0), lugar(1, 1), lugar(2, 1)]
        }
			


class bloque5(Bloques):
		def __init__(self):
			super().__init__(id = 5)
			self.cells = {
				0: [lugar(0, 0), lugar(1, 0), lugar(0, 1), lugar(1, 1)],
            	1: [lugar(0, 0), lugar(0, 0), lugar(0, 0), lugar(0, 0)],
            	2: [lugar(0, 0), lugar(0, 0), lugar(0, 0), lugar(0, 0)],
            	3: [lugar(0, 0), lugar(0, 0), lugar(0, 0), lugar(0, 0)]
			}

class bloque6(Bloques):
		def __init__(self):
			super().__init__(id = 5)
			self.cells = {
	            0: [lugar(0, 1), lugar(1, 0), lugar(1, 1), lugar(1, 2)],
	            1: [lugar(0, 1), lugar(1, 1), lugar(1, 2), lugar(2, 1)],
	            2: [lugar(1, 0), lugar(1, 1), lugar(1, 2), lugar(2, 1)],
	            3: [lugar(0, 1), lugar(1, 0), lugar(1, 1), lugar(2, 1)]
	        }

class bloque7(Bloques):
		def __init__(self):
			super().__init__(id = 7)
			self.cells = {
	            0: [lugar(0, 0), lugar(0, 1), lugar(1, 1), lugar(1, 2)],
	            1: [lugar(0, 2), lugar(1, 1), lugar(1, 2), lugar(2, 1)],
	            2: [lugar(1, 0), lugar(1, 1), lugar(2, 1), lugar(2, 2)],
	            3: [lugar(0, 1), lugar(1, 0), lugar(1, 1), lugar(2, 0)]
	        }

def seleccion_bloque(self):
    if len(self.bloque) == 0:
        self.bloque = [Bloque1(), Bloque2(), Bloque3(), Bloque4(), Bloque6(), Bloque7(), Bloque8()]
    
    bloque = random.choice(self.bloque)
    self.bloque.remove(bloque)
    
    return bloque


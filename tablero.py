class Tablero:
    def __init__(self):
        self.num_filas = 20
        self.num_columnas = 10
        self.cell_size = 30
        self.tab = [[0 for j in range(self.num_columnas)] for i in range(self.num_filas)]
        self.colores = self.seleccion_colores()

    def print_tab(self):
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                print(self.tab[fila][columna], end = " ")
            print()

    def seleccion_colores(self):
        Gris = (25, 30, 40)
        Azul = (15, 65, 220)
        Rojo = (230, 20, 20)
        Verde = (50, 230, 25)
        Cyan = (20, 205, 210)
        Morado = (165, 0, 250)
        Amarillo = (235, 235, 5)
        Blanco = (255, 255, 255)

        return [Gris, Azul, Rojo, Verde, Cyan, Morado, Amarillo, Blanco]
"""
    def draw(self):
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                cell value = self.grid[fila][columna]
                cell_rect = pygame.Rect(columna*self.cell_size, fila*self.cell_size, 
                self.cell_size, self.cell_size)
                #pygame.draw.rect(screen, colores, rect)
                """


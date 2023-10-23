# PCI-PROYECTO TETRIS

Clase: Pensamiento Computacional para Ingenieria 

Por: Juan Jose Goyeneche Sanchez

El Proyecto sera un juego de Tetris con diferentes velocidades, programado en Python para la clase de Pensamiento Computacional para Ingenieria.
Se usan 4 modulos:
Main para llamar a ejecutar el programa principalmente
Tablero: Para crear el tablero, celdas y toda la pantalla.
Blokes: Para crear la estructura de los bloques y sus "Fisicas"
Game: Para crear las "secuencias" del juego-
Para este proyecto tuve que adentrarme en "PYGAME", Pygame es una biblioteca de código abierto en Python que proporciona herramientas y funciones para el desarrollo de videojuegos y aplicaciones multimedia. Al ser una biblioteca relativamente nueva para mi este proyecto consto de una gran parte de investigacion sobre como usar pygame siendo de ayuda la pagina https://www.pygame.org/. La parte mas complicada del programa fueron los bloques buscando ideas encontre super init, que crea una "super clase" en la cual puede entrar otra clase por asi decirlo. De esta manera pude crear los bloques por su cuenta y agregarles valores ya predeterminado anteriormente, esta fue la parte que mas investigacion y ejemplos varios requirio.
Al final el programa aun tiene varias imperfecciones como que la funcion que imprime siguiente bloque no lo hace con precision. pero en mi opinion ya son nimiedades y yo estoy muy satisfecho con el resultado del programa.
Al tener cierto conocimiento previo de Python decidi hacer un proyecto que involucre un reto diferente e investigacion de cosas aparte de la clase.

*Nota1: Para probar el programa sera necesario instalar e importar pygame, random, sys.

*Nota2: Hay un archivo wav que no puedo subir al repositorio por su peso ("Tetris.py\MOONDOG Birds Lament.remix.wav") por lo cual recomiendo borrar las lineas relacionadas con la musica, o de existir alguna manera de que mande el archivo lo hare. 
Link para descargar el archivo Wav faltante: https://soundcloud.com/charliefauv/moondog-birds-lament


=================================================================

Correcciones
Componente: plantea una situación problema que le permite aplicar y demostrar sus conocimientos de programación (avance 1)
  error: Falta de algoritmo del proyecto
  Correccion: Gran parte del codigo viene con comentarios aclarando los pasos y las funcionalidades de las lineas de codigo.
  Ejemplo: 
  # Creación de la pantalla
# Musica y Volumen
# Tablero y decoracion (tablero.py)
# Funcionalidad (Game.py) Etc...

componente: usa operadores aritméticos de manera eficaz (avance 2)
  error: No hubo entrega
  *Nota: Aqui la confusion fue mia, tras la primera entrega del link yo pense que para los siguientes avances se revisarian usando el mismo link (no sabia que debia de volver a enviarlo por canvas), pero en la entrega final se puede ver como los operadores aritmeticos se emplean en el codigo.  
  ejemplo: 
      def dibujar_cuadro_contorno(pantalla, x, y):
        negro = (0, 0, 0)
        verde = (0, 255, 0)
        horizontal = 185
        vertical = 135
        cuerpo = 5
        pygame.draw.rect(pantalla, negro, (x, y, horizontal, vertical), cuerpo)
        pygame.draw.line(pantalla, verde, (x, y + vertical // 2), (x + horizontal, y + vertical // 2), cuerpo)

componente: aplica estructuras condicionales para resolver un problema (avance 4)
  error: No hubo entrega
  *Nota: Aqui la confusion fue mia, tras la primera entrega del link yo pense que para los siguientes avances se revisarian usando el mismo link (no sabia que debia de volver a enviarlo por canvas), pero en la entrega final se puede ver como si se usan condicionantes if y else en el codigo.  
  ejemplo: 
    def fila_completa(self):
        completadas = 0
        for fila in range(self.num_filas - 1, 0, -1):
            if all(self.tab[fila]):
                self.eliminar_fila(fila)
                completadas += 1
            elif completadas > 0:
                self.bajar(fila, completadas)
        return completadas
  
  
componente: aplica estructuras cíclicas para resolver un problema de manera eficiente (avance 5)
  error: No hubo entrega
  *Nota: Aqui la confusion fue mia, tras la primera entrega del link yo pense que para los siguientes avances se revisarian usando el mismo link (no sabia que debia de volver a enviarlo por canvas), pero en la entrega final se puede ver como los ciclos While y For in se emplean en el codigo.  
  ejemplo:  def __init__(self): #Inicializar Tablero
        self.cell_size = 40 #Tamaño Celdas
        self.num_filas = 20 
        self.num_columnas = 10
        self.colores = self.seleccion_colores()
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
        # Print self.tab
    def imprimir_celdas(self):
        for fila in self.tab:
            for celda in fila:
                print(celda, end=" ")
            print() 

 




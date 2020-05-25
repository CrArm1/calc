import os
from turtle import *

# Posicion de la ventana ancho, alto, posicionX, posicionY 
setup(800, 800, 500, 100)
# Area de dibujo
screensize(800, 800)
# Color del trazo
colormode(255)
# No muestra los trazos

'''
DIBUJO DEL PLANO
goto(posX, posY)    =====> posicion de los puntos x - y en la pantalla
'''
# Dibujo del eje de las ordenadas o Y
goto(0,-800)
goto(0,800)
# Levanta o pausa el trazo

# Dibujo del eje de las abscisas o X
penup()         # Levanta el trazo
goto(800, 0)    # Linea que no se dibuja
pendown()       # Activa el trazo
goto(800, 0)
goto(-800, 0)
penup()

os.system("pause")

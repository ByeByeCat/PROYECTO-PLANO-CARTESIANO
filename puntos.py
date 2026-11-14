# puntos.py
# Punto 1 del proyecto: listas con conjuntos de puntos para proyectar
# en un plano cartesiano.
#
# Convenciones:
#   - Cada punto es una tupla (x, y) con coordenadas enteras.
#   - Cada lista tiene minimo 4 puntos y no repite puntos.
#   - Hay minimo 4 listas de prueba (aqui son 5).

# Lista 1: los puntos de la Figura 2 del enunciado.
LISTA_1 = [(1, 1), (1, 5), (5, 1), (1, -2), (5, -2)]

# Lista 2: los puntos de la Figura 1 del enunciado (9 puntos, incluye
# coordenadas grandes y negativas para probar el dibujo del plano).
LISTA_2 = [(3, 20), (14, 9), (4, 5), (3, 2), (15, 2),
           (-4, -5), (7, -5), (24, -5), (7, -24)]

# Lista 3: contiene un cuadrado de lado 4 y un punto aislado.
LISTA_3 = [(-3, -3), (1, -3), (1, 1), (-3, 1), (6, 5)]

# Lista 4: contiene un triangulo acutangulo claro: (0,0), (4,0), (2,3).
LISTA_4 = [(0, 0), (4, 0), (2, 3), (-2, -5)]

# Lista 5: puntos colineales; no se puede formar ninguna figura.
LISTA_5 = [(0, 0), (1, 1), (2, 2), (3, 3)]

# Conjunto de todas las listas, para que el menu del programa principal
# pueda escoger cual proyectar.
LISTAS_DE_PUNTOS = [LISTA_1, LISTA_2, LISTA_3, LISTA_4, LISTA_5]

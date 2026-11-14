# figuras.py
# Punto 2 del proyecto: determinar si con los puntos de una lista se
# pueden formar un rectangulo, un cuadrado, un triangulo acutangulo y
# un triangulo rectangulo.
#
# Solo aritmetica entera (sin raices, sin librerias).
# Un punto es una tupla (x, y). Los puntos de una lista son distintos.


# ---------------------------------------------------------------
# Algoritmos auxiliares (costo O(1) cada uno)
# ---------------------------------------------------------------

def dist_cuad(p, q):
    """Distancia al cuadrado entre p y q."""
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return dx * dx + dy * dy


def prod_punto(v, p, q):
    """Producto punto de los vectores v->p y v->q (angulo en el vertice v).
    = 0 : angulo recto   > 0 : angulo agudo   < 0 : angulo obtuso"""
    return (p[0] - v[0]) * (q[0] - v[0]) + (p[1] - v[1]) * (q[1] - v[1])


def es_rectangulo_ordenado(a, b, c, d):
    """Verdadero si a-b-c-d (en ese orden) tiene sus 4 angulos rectos."""
    if prod_punto(b, a, c) != 0:
        return False
    if prod_punto(c, b, d) != 0:
        return False
    if prod_punto(d, c, a) != 0:
        return False
    if prod_punto(a, d, b) != 0:
        return False
    return True


def es_rectangulo_4(p0, p1, p2, p3):
    """Verdadero si los 4 puntos forman un rectangulo en algun orden.
    Fijando p0, hay 3 ciclos distintos."""
    return (es_rectangulo_ordenado(p0, p1, p2, p3)
            or es_rectangulo_ordenado(p0, p1, p3, p2)
            or es_rectangulo_ordenado(p0, p2, p1, p3))


def es_cuadrado_ordenado(a, b, c, d):
    """Rectangulo a-b-c-d con dos lados consecutivos iguales."""
    if not es_rectangulo_ordenado(a, b, c, d):
        return False
    return dist_cuad(a, b) == dist_cuad(b, c)


def es_cuadrado_4(p0, p1, p2, p3):
    """Verdadero si los 4 puntos forman un cuadrado en algun orden."""
    return (es_cuadrado_ordenado(p0, p1, p2, p3)
            or es_cuadrado_ordenado(p0, p1, p3, p2)
            or es_cuadrado_ordenado(p0, p2, p1, p3))


def es_triangulo_rectangulo(a, b, c):
    """Verdadero si alguno de los 3 angulos es recto."""
    return (prod_punto(a, b, c) == 0
            or prod_punto(b, a, c) == 0
            or prod_punto(c, a, b) == 0)


def es_triangulo_acutangulo(a, b, c):
    """Verdadero si los 3 angulos son agudos."""
    return (prod_punto(a, b, c) > 0
            and prod_punto(b, a, c) > 0
            and prod_punto(c, a, b) > 0)


# ---------------------------------------------------------------
# Algoritmos del punto 2 (existencia de cada figura en la lista)
# ---------------------------------------------------------------

def existe_rectangulo(lista):
    n = len(lista)
    for i in range(0, n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if es_rectangulo_4(lista[i], lista[j], lista[k], lista[l]):
                        return True
    return False


def existe_cuadrado(lista):
    n = len(lista)
    for i in range(0, n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if es_cuadrado_4(lista[i], lista[j], lista[k], lista[l]):
                        return True
    return False


def existe_triangulo_rectangulo(lista):
    n = len(lista)
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if es_triangulo_rectangulo(lista[i], lista[j], lista[k]):
                    return True
    return False


def existe_triangulo_acutangulo(lista):
    n = len(lista)
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if es_triangulo_acutangulo(lista[i], lista[j], lista[k]):
                    return True
    return False


# ---------------------------------------------------------------
# Prueba rapida
# ---------------------------------------------------------------
if __name__ == "__main__":
    from puntos import LISTAS_DE_PUNTOS

    numero = 1
    for lista in LISTAS_DE_PUNTOS:
        print("Lista", numero, lista)
        print("  Rectangulo:          ", existe_rectangulo(lista))
        print("  Cuadrado:            ", existe_cuadrado(lista))
        print("  Triangulo acutangulo:", existe_triangulo_acutangulo(lista))
        print("  Triangulo rectangulo:", existe_triangulo_rectangulo(lista))
        numero = numero + 1

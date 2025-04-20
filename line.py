import math
def line():
    def obtener_flotante(mensaje):
        return float(input(mensaje))

    A = obtener_flotante("Ingrese el coeficiente A: ")
    B = obtener_flotante("Ingrese el coeficiente B: ")
    X1 = obtener_flotante("Ingrese el valor de X1: ")
    X2 = obtener_flotante("Ingrese el valor de X2: ")

    Y1 = A * X1 + B
    Y2 = A * X2 + B

    print(f"\nLa ecuación de la recta es: Y = {A}X + {B}")
    print(f"\nPuntos calculados:")
    print(f"\tP1 ({X1}, {Y1})")
    print(f"\tP2 ({X2}, {Y2})")

    dist = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
    print(f"\nLa distancia entre P1 y P2 es: {dist}")

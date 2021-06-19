from Figuras import Punto, Circunferencia

c = Circunferencia()
c.setCentro(1, 1)
c.setRadio(3)
print(c)
puntos = [[1, 2], [-1, 2], [-1, -2], [3, 3], [-2, 4]]
objPuntos = []
for pto in puntos:
    x, y = pto
    p = Punto()
    p.setX(x)
    p.setY(y)
    objPuntos.append(p)
for p in objPuntos:
    print(c.interior(p))

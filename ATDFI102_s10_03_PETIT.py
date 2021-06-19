from Figuras import Punto

p = Punto()
q = Punto()
p.setX(6)
p.setY(3)
q.setX(3)
q.setY(6)
print(p)
print(q)
print(p.cuadrante())
print(q.cuadrante())
print(p.distanciaEuclidiana(q))

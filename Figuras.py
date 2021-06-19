from math import sqrt
import math


class Punto(object):
    x: int
    y: int

    def __init__(self):
        return

    def __str__(self):
        return "("+str(self.x)+"," + str(self.y)+")"

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def cuadrante(self):
        if(self.x >= 0 and self.y >= 0):
            return 1
        if(self.x >= 0 and self.y <= 0):
            return 4
        if(self.x <= 0 and self.y >= 0):
            return 2
        if(self.x <= 0 and self.y <= 0):
            return 3

    def distanciaEuclidiana(self, punto):
        a = abs((punto.getX() - self.x) ^ 2)
        b = abs((punto.getY() - self.y) ^ 2)
        de = round(sqrt(a + b), 2)
        return de


class Circunferencia():
    centro: Punto
    radio: int

    def __init__(self):
        self.centro = Punto()
        return

    def __str__(self):
        return "Centro: "+str(self.centro)+" , Radio: "+str(self.radio)

    def getCentro(self):
        return self.centro

    def setCentro(self, x, y):
        self.centro.setX(x)
        self.centro.setY(y)

    def setRadio(self, radio):
        self.radio = radio

    def getRadio(self):
        return self.radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def interior(self, point: Punto):
        distancia = sqrt((point.getX() - self.getCentro().getX())
                         ** 2 + (point.getY() - self.getCentro().getY())**2)
        if(distancia < self.radio):
            return True
        else:
            return False

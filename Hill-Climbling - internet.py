import math

incremento = 0.1
stdInicial = [1,1]
point1 = [1,5]
point2 = [6,4]
point3 = [5,2]
point4 = [2,1]


# Calcula a distâcia entre dois pontos (x1,y1) e (x2,y2)
def distancia(x1, y1, x2, y2):
    dist = math.pow(x2-x1, 2) + math.pow(y2-y1, 2)
    return dist

# Dado um ponto (x1, y1), calcula a soma das distâncias desse ponto até outros quatro pontos
def SomaDasDists(x1, y1, px1, py1, px2, py2, px3, py3, px4, py4):
    d1 = distancia(x1, y1, px1, py1)
    d2 = distancia(x1, y1, px2, py2)
    d3 = distancia(x1, y1, px3, py3)
    d4 = distancia(x1, y1, px4, py4)

    return d1 + d2 + d3 + d4

# Retorna o ponto seguido da soma das distâncias desse ponto a outros quatro pontos
def novaDistacia(x1, y1, point1, point2, point3, point4):
    d1 = [x1, y1]
    d1temp = SomaDasDists(x1, y1, point1[0], point1[1], point2[0], point2[1], point3[0], point3[1], point4[0], point4[1])

    d1.append(d1temp)
    return d1


def novosPontos(minimo, d1, d2, d3, d4):
    if d1[2] == minimo:
        return [d1[0], d1[1]]
    elif d2[2] == minimo:
        return [d2[0], d2[1]]
    elif d3[2] == minimo:
        return [d3[0], d3[1]]
    elif d4[2] == minimo:
        return [d4[0], d4[1]]


distanciaMin = SomaDasDists(stdInicial[0], stdInicial[1], point1[0], point1[1], point2[0], point2[1], point3[0], point3[1], point4[0], point4[1])
controle = True

i = 1

while controle:

    d1 = novaDistacia(stdInicial[0]+incremento, stdInicial[1], point1, point2, point3, point4)
    d2 = novaDistacia(stdInicial[0]-incremento, stdInicial[1], point1, point2, point3, point4)
    d3 = novaDistacia(stdInicial[0], stdInicial[1]+incremento, point1, point2, point3, point4)
    d4 = novaDistacia(stdInicial[0], stdInicial[1]-incremento, point1, point2, point3, point4)

    print(str(i) + ' ' + str(round(stdInicial[0], 2)) + ' ' + str(round(stdInicial[1], 2)))
    minimo = min(d1[2], d2[2], d3[2], d4[2])

    if minimo < distanciaMin:
        stdInicial = novosPontos(minimo, d1, d2, d3, d4)
        distanciaMin = minimo

        i += 1

    else:
        controle = False

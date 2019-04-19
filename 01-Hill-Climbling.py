# Implementação do algoritmo Hill Climbling, que acha o máximo local de uma dada função f(x, y)
# onde x e y pertecem ao intervalo de 0 a 20

import math
from random import uniform

incremento = 0.01

# Dois valores aleatótios para x e y
# pertencentes ao intervalo [0, 20]
pontoInicial = [uniform(0,20), uniform(0,20)]


# Função dada no problema
# p = [x, y]
def f(p):

    func = abs( (p[0] * math.sin((p[1] * math.pi) / 4)) + (p[1] * math.sin((p[0] * math.pi) / 4)) )

    return func


# Retorna todos os vizinhos de um ponto dado
def novosVizinhos(p):
    v1 = [p[0] + incremento, p[1] + incremento]
    v2 = [p[0] - incremento, p[1] - incremento]
    v3 = [p[0] - incremento, p[1] + incremento]
    v4 = [p[0] + incremento, p[1] - incremento]

    return v1, v2, v3, v4

# Retorna o ponto cujo falor da função é máximo e um valor booleano que informa
# True se o ponto dado é um máximo local e False caso não seja.
def otimiza(ponto, v1, v2, v3, v4 ):
    f_p = f(ponto)
    f1 = f(v1)
    f2 = f(v2)
    f3 = f(v3)
    f4 = f(v4)

    values = [f_p, f1, f2, f3, f4]

    maximo = max(values)

    index_max = values.index(maximo)

    if index_max == 0:
        return ponto, True # Nesse caso o algoritmo deve parar, pois ele é o máximo de todos os seus vizinhos
    elif index_max == 1:
        return v1, False
    elif index_max == 2:
        return v2, False
    elif index_max == 3:
        return v3, False
    elif index_max == 4:
        return v4, False


controle_laco = False
ponto_atual = pontoInicial
while controle_laco == False:

    v_1, v_2, v_3, v_4 = novosVizinhos(ponto_atual)

    ponto_atual, controle_laco = otimiza(ponto_atual, v_1, v_2, v_3, v_4)
    print('Ponto atual: [%s, %s] \n f(x,y) = %s' % (str(ponto_atual[0]), str(ponto_atual[1]), str(f(ponto_atual))))

print("Deu certo!!")
print('Ponto inicial: [%s, %s]' % (str(pontoInicial[0]), str(pontoInicial[1])))

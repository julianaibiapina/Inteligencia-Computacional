import math
from random import uniform
import numpy as np
import matplotlib.pyplot as plt
import itertools

# Função y() que retorna 1 ou 0 dependendo se u >0 ou u<=0
def func_y(ax):
    if ax>0:
        return 1
    elif ax<0 or u==0:
        return 0


# Entrada: todas as possibilidade de x_1 e X_2
x_1 = np.array([0, 0, 1, 1])
x_2 = np.array([0, 1, 0, 1])
# Saída: o resultado esperado
d = np.array([0, 1, 1, 1])

# passo de aprendizagem
n= 0.5

# cria vetor de pesos e limiar
w = np.array([0, 0, 0])

cont = 0 # conta as iterações
u = 0    # amazena os produtos escalares de casa iteração
aux = np.empty(3)
y = np.zeros(d.shape[0])

controle = False # controle de laço
while controle == False:
    for i in range(0, x_1.shape[0]):

        print('Entradas: \nx_1: %d e x_2: %d' % (x_1[i], x_2[i]))
        # vetor de entrada x
        x = np.array([-1, x_1[i], x_2[i]])

        if cont == 0:
            u = np.dot(x.transpose(), w)       # retorna um escalar
        else:
            u = np.dot(x.transpose(), w[cont]) # retorna um escalar
        y[i] = func_y(u)
        e = d[i] - y[i]
        #soma os elementos de posições correspondentes(axis=0 -> linha com linha)
        if cont == 0:
            aux = np.sum((w, np.dot((n * e), x) ), axis=0)
        else:
            aux = np.sum((w[cont], np.dot((n * e), x) ), axis=0)
        w = np.vstack((w,aux))
        print(w)
        cont +=1
    # o laço 'while' só para quando o vetor 'y' for igual ao vetor esperado 'd'
    comp = 0
    for aux1, aux2 in itertools.zip_longest(d, y):
        if (aux1 == aux2):
            comp = comp + 1
    if comp == d.shape[0]:
        print(y)
        controle = True
print('Pesos obtidos: ')
print(w[w.shape[0]-1])

# TESTANDO
print('TESTE')
vet_teste = np.array([-1, 0, 0])
result = np.dot(w[w.shape[0]-1], vet_teste)
if result>0:
    print('1')
elif result == 0 or result < 0:
    print('0')

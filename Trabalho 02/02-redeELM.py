import math
import random
import numpy as np
import matplotlib.pyplot as plt
import itertools


data = np.loadtxt('./Trabalho 02/iris_log.dat')
x_treino = data[0:105, 0:4] # características (70% dos dados)
x_treino = x_treino.transpose()
ones = np.ones(x_treino.shape[1])
x_treino = np.vstack((ones, x_treino))


y_treino = data[0:105, 4:] # (70% dos dados)
y_treino = y_treino.transpose()

#x_treino = x_treino.reshape((4, 150)) # transforma em um vetor de N colunas

# q = quantidade de neurônios
q = 10
# p = quantidade de variáveis de entrada
p = 4

# vetor de pesos da camada oculta
W = np.random.rand(q, p+1) * 0.1

# ativações dos neurônios da camada oculta
u = np.matmul(W, x_treino)


Z = np.empty(u.shape)
for i in range(0, u.shape[0]):
    for j in range(0, u.shape[1]):
        Z[i,j] = 1 / (1 + math.exp(-1 * u[i, j]))


# saídas das camadas ocultas acrescentada com uma linha de 1's
Z = np.vstack((ones, Z))

# pesos da camada de saída
aux1 = np.matmul(y_treino, Z.transpose())
aux2 = np.linalg.inv(np.matmul(Z, Z.transpose()))
M = np.matmul(aux1, aux2)


#Y = np.matmul(M, Z)


# TESTE: Hold-Out
x_teste = data[105:, 0:4] # características (30% dos dados)

x_teste = x_teste.transpose()
ones = np.ones(x_teste.shape[1])
x_teste = np.vstack((ones, x_teste))

y_teste = data[105:, 4:] # (30% dos dados)
y_teste = y_teste.transpose()

u_teste = np.matmul(W,x_teste)

Z_teste = np.empty(u_teste.shape)
for i in range(0, u_teste.shape[0]):
    for j in range(0, u_teste.shape[1]):
        Z_teste[i,j] = 1 / (1 + math.exp(-1 * u_teste[i, j]))

ones = np.ones(x_teste.shape[1])
Z_teste = np.vstack((ones, Z_teste))


Y_teste = np.matmul(M, Z_teste)

for i in range(0, Y.shape[1]):
    print(Y[0:, i:i+1])

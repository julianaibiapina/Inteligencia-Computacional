import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')




#------------------------GRÁFICO------------------------
data_plot = np.loadtxt('./Trabalho 03/twomoons.dat')
x_1Plot = data_plot[0:, 0:1]
x_2Plot = data_plot[0:, 1:2]
rotuloPlot = data_plot[0:, 2:3]
# CLASSE A = 0:501
# CLASSE B = 501:

#----------------------TREINAMENTO----------------------
# Embaralha os dados para o treinamento
data = np.random.permutation(data_plot)
x_treino = data[0:, 0:2]
x_treino = x_treino.transpose() # transforma linhas em colunas
ones = np.ones(x_treino.shape[1])
x_treino = np.vstack((ones, x_treino)) # empilha o vetor de 1's em cima do vetor de entradas

rotulo = data[0:, 2:3]
rotulo = rotulo.transpose() # transforma em um vetor colunas

# q = quantidade de neurônios
q = 10
# p = quantidade de variáveis de entrada
p = 2

# vetor de pesos da camada oculta
W = np.random.rand(q, p+1) * 0.1


# ativações dos neurônios da camada oculta
u = np.matmul(W, x_treino)

# Vetor Z de saídas da camada oculta
Z = np.empty(u.shape)
for i in range(0, u.shape[0]):
    for j in range(0, u.shape[1]):
        Z[i,j] = 1 / (1 + math.exp(-1 * u[i, j]))

# saídas da camada oculta acrescentada com uma linha de 1's
Z = np.vstack((ones, Z))

# pesos da camada de saída
aux1 = np.matmul(rotulo, Z.transpose())
aux2 = np.linalg.inv(np.matmul(Z, Z.transpose()))
M = np.matmul(aux1, aux2)

# Vetor de saídas calculadas pelo modelo
Y = np.matmul(M, Z)



# CLASSE A
ax.scatter(x_1Plot[0:501], x_2Plot[0:501], rotuloPlot[0:501], c='r', marker='o')
# CLASSE B
ax.scatter(x_1Plot[501:], x_2Plot[501:], rotuloPlot[501:], c='b', marker='^')
#Classificação da Rede ELM
ax.scatter(data[0:, 0:1], data[0:, 1:2], Y[0:], c='g', marker='^')


ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('Rótulo')
plt.show()

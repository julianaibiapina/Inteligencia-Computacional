import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools


data_plot = np.loadtxt('./Trabalho 03/twomoons.dat')


# Embaralha os dados para o treinamento
data = np.random.permutation(data_plot)

#----------------------TREINAMENTO----------------------

x_treino = data[0:, 0:2]
x_treino = x_treino.transpose()
ones = np.ones(x_treino.shape[1])
x_treino = np.vstack((ones, x_treino))

rotulo = data[0:, 2:]
rotulo = rotulo.transpose()

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

result = list()
cont1 = 0
cont2 = 0
for i in Y[0]:
    if i>0:
        result.append(1)
        cont1 += 1
    elif i<0 or i==0:
        result.append(-1)
        cont2 +=1

result = np.array(result)
result = result.reshape((1001, 1))

# -------------------Teste do Classificador
# intervalo de valores de x1
min1 = np.amin(data[0:, 0:1])
max1 = np.amax(data[0:, 0:1])
intevalo_x1 = np.linspace(min1, max1, 100)

# intervalo de valores de x2
min2 = np.amin(data[0:, 1:2])
max2 = np.amax(data[0:, 1:2])
intevalo_x2 = np.linspace(min2, max2, 100)

# cria vetor que percorre toda a área
aux = list()
# vetor para percorrer todo o espaço da amostra
for i in intevalo_x1:
    for j in intevalo_x2:
        aux.append([i,j])

# array que possui todos os pontos percorrendo a área desejada
aux = np.array(aux)

x = aux.transpose()
ones = np.ones(x.shape[1])
x =  np.vstack((ones, x))

# ativações dos neurônios da camada oculta
u_teste = np.matmul(W, x)

# Vetor Z de saídas da camada oculta
Z_teste = np.empty(u_teste.shape)
for i in range(0, u_teste.shape[0]):
    for j in range(0, u_teste.shape[1]):
        Z_teste[i,j] = 1 / (1 + math.exp(-1 * u_teste[i, j]))

# saídas da camada oculta acrescentada com uma linha de 1's
Z_teste = np.vstack((ones, Z_teste))

Y_teste = np.matmul(M, Z_teste)


result_teste = list()
cont1 = 0
cont2 = 0
for i in Y_teste[0]:
    if i>-0.5 and i<0.5:
        print(i)
    if i>0:
        result_teste.append(1)
        cont1 += 1
    elif i<0 or i==0:
        result_teste.append(-1)
        cont2 +=1


result_teste = np.array(result_teste)
result_teste = result_teste.reshape((10000, 1))
print(result_teste.shape)



# -------------- Gráfico
# OBS: colocar título no gráfico.

plt.figure(1) # plot do teste com os dados de treinamento
plt.scatter(data[0:, 0:1], data[0:, 1:2],  c=result, s=7)
plt.figure(2) # plot dos dados originais
plt.scatter(data[0:, 0:1], data[0:, 1:2],  c=data[0:, 2:3], s=7)
plt.figure(3) # plot dos dados originais
plt.scatter(aux[0:, 0:1], aux[0:, 1:2],  c=result_teste, s=7)
plt.show()

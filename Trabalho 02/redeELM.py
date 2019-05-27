import math
import random
import numpy as np
import matplotlib.pyplot as plt
import itertools

data = np.loadtxt('./Trabalho 02/aerogerador.dat')
x_treino = data[0:, 0:1] # velociade do vento

y_treino = data[0:, 1:]  # potência


# DOIS NEURÔNIOS NA CAMADA OCULTA

# Vetor de pesos inicial preenchido com valores aleatórios uniformente distribídos no intervalo [-1, 1)
aux = [random.uniform(0, 1), random.uniform(0, 1)]
W = np.array(aux) # matriz de pesos
Z = np.array([[], []])  # matriz de saídas
for i in range(0, x_treino.shape[0]):
    x = x_treino[i]
    u =  np.dot(W, x[0])
    z = np.array([[(1 / (1 + (math.exp(-1 * u[0]))))], [(1 / (1 + (math.exp(-1 * u[1]))))]])
    Z = np.hstack((Z,z))

# vetor D de saídas esperadas
D = y_treino.reshape((1, 2250))

# matriz M de pesos da camada de saída
M = np.matmul(D,Z.transpose())
M = np.matmul(M,np.linalg.inv(np.matmul(Z,Z.transpose())))


# O vetor Y guarda os valores y de saída da última camada para casa amostra
Y_list = list()
for i in range(0, x_treino.shape[0]):

    input = Z[0:, i:(i+1)]
    y = np.dot(M, input)[0][0]
    Y_list.append(y)
Y = np.array(Y_list)
print(Y.shape)
# plotando
plt.figure(1)
plt.scatter(x_treino, y_treino)   # amostras
plt.plot(x_treino, Y[0:], color = 'red') # regressão linear
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Teste')
plt.grid(True)

plt.show()

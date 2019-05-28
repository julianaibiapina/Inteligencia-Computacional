import math
import random
import numpy as np
import matplotlib.pyplot as plt
import itertools

data = np.loadtxt('./Trabalho 02/aerogerador.dat')
x_treino = data[0:, 0:1] # velociade do vento
x_treino = x_treino.reshape((1, 2250)) # transforma em um vetor de N colunas
ones = np.ones(x_treino.shape)
x_treino = np.vstack((ones, x_treino)) # acrescenta uma linha de 1's

y_treino = data[0:, 1:]  # potência
y_treino = y_treino.reshape((1, 2250)) # transforma em um vetor de N colunas

#numero de neurônios da camada oculta
q = 2
p = 1 # número de variáveis de entrada

# vetor de pesos da camada oculta
W = np.random.rand(q, p+1) # matriz de pesos

# ativações dos neurônios da camada oculta
u = np.matmul(W, x_treino)

Z = np.array([[],[]])
#percorrer todas as N colunas de u
for i in range(0, u.shape[1]):
    z = np.array([[(1 / (1 + (math.exp(-1 * u[0:1, i:i+1][0][0]))))], [(1 / (1 + (math.exp(-1 * u[1:2, i:i+1][0][0]))))]])
    #print(z)
    Z = np.hstack((Z,z))

# vetor Z que é a entrada da camada de saída
ones = np.ones((1, Z.shape[1]))
Z = np.vstack((ones, Z)) # acrescenta uma linha de 1's


# vetor M de pesos da camada de saída
aux = np.matmul(y_treino, Z.transpose())
aux2 = np.linalg.inv(np.matmul(Z, Z.transpose()))
M = np.matmul(aux, aux2)

# vetor final com os resultados da camda de saída
y = np.matmul(M,Z)


# Gráfico
plt.figure(1)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(data[0:, 0:1], y.transpose(), color = 'red') # rede neural
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Dois neurônios na camada oculta')
plt.grid(True)

plt.show()

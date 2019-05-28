import math
import random
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('./Trabalho 02/aerogerador.dat')
x_treino = data[0:, 0:1] # velociade do vento
x_treino = x_treino.reshape((1, 2250)) # transforma em um vetor de N colunas
ones = np.ones(x_treino.shape)
x_treino = np.vstack((ones, x_treino)) # acrescenta uma linha de 1's

y_treino = data[0:, 1:]  # potência
y_treino = y_treino.reshape((1, 2250)) # transforma em um vetor de N colunas

q1 = 1
q2 = 2 # número de neurônios da camada oculta
p = 1 # número de variáveis de entrada

#---------------------------------- 1 NEURÔNIO

# vetor de pesos da camada oculta
W1 = np.random.rand(q1, p+1) # matriz de pesos onde cada elemento varia num intervalo de (0,1) em uma distribuição uniforme

# ativações dos neurônios da camada oculta
u1 = np.matmul(W1, x_treino)

Z1 = np.array([[]]) # um neurônios

# percorrer todas as N colunas de u
for i in range(0, u1.shape[1]):
    z1 = np.array([[(1 / (1 + (math.exp(-1 * u1[0:1, i:i+1][0][0]))))]])
    Z1 = np.hstack((Z1,z1))

# vetor Z1 que é a entrada da camada de saída
ones = np.ones((1, Z1.shape[1]))
Z1 = np.vstack((ones, Z1)) # acrescenta uma linha de 1's

# vetor M1 de pesos da camada de saída
aux = np.matmul(y_treino, Z1.transpose())
aux2 = np.linalg.inv(np.matmul(Z1, Z1.transpose()))
M1 = np.matmul(aux, aux2)

# vetor final com os resultados da camasda de saída
y1 = np.matmul(M1,Z1)


#---------------------------------- 2 NEURÔNIOS

# vetor de pesos da camada oculta
W = np.random.rand(q2, p+1) # matriz de pesos onde cada elemento varia num intervalo de (0,1) em uma distribuição uniforme

# ativações dos neurônios da camada oculta
u = np.matmul(W, x_treino)


Z = np.array([[],[]]) # dois neurônios
#percorrer todas as N colunas de u
for i in range(0, u.shape[1]):
    z = np.array([[(1 / (1 + (math.exp(-1 * u[0:1, i:i+1][0][0]))))], [(1 / (1 + (math.exp(-1 * u[1:2, i:i+1][0][0]))))]])
    Z = np.hstack((Z,z))

# vetor Z que é a entrada da camada de saída
ones = np.ones((1, Z.shape[1]))
Z = np.vstack((ones, Z)) # acrescenta uma linha de 1's


# vetor M de pesos da camada de saída
aux = np.matmul(y_treino, Z.transpose())
aux2 = np.linalg.inv(np.matmul(Z, Z.transpose()))
M = np.matmul(aux, aux2)

# vetor final com os resultados da camada de saída
y = np.matmul(M,Z)


# Gráfico
# 2 NEURÔNIOS
plt.figure(1)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(data[0:, 0:1], y.transpose(), color = 'red') # rede neural
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Dois neurônios na camada oculta')
plt.grid(True)

# 1 NEURÔNIO
# Gráfico
plt.figure(2)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(data[0:, 0:1], y1.transpose(), color = 'red') # rede neural
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Um neurônio na camada oculta')
plt.grid(True)

plt.show()

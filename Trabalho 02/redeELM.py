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

# número de neurônios da camada oculta
q1 = 1
q2 = 2
q3 = 3
q4 = 4
p = 1 # número de variáveis de entrada

#---------------------------------- 1 NEURÔNIO

# vetor de pesos da camada oculta
W1 = np.random.rand(q1, p+1) * 0.1# matriz de pesos onde cada elemento varia num intervalo de (0,1) em uma distribuição uniforme

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
W = np.random.rand(q2, p+1) * 0.1 # matriz de pesos onde cada elemento varia num intervalo de (0,1) em uma distribuição uniforme

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

#---------------------------------- 3 NEURÔNIOS

# vetor de pesos da camada oculta
W3 = np.random.rand(q3, p+1) * 0.1 # matriz de pesos onde cada elemento varia num intervalo de (0,1) em uma distribuição uniforme

# ativações dos neurônios da camada oculta
u3 = np.matmul(W3, x_treino)

Z3 = np.array([[], [], []]) # três neurônios

# percorrer todas as N colunas de u
for i in range(0, u3.shape[1]):
    z3 = np.array([[(1 / (1 + (math.exp(-1 * u3[0:1, i:i+1][0][0]))))], [(1 / (1 + (math.exp(-1 * u3[1:2, i:i+1][0][0]))))], [(1 / (1 + (math.exp(-1 * u3[2:3, i:i+1][0][0]))))]])
    Z3 = np.hstack((Z3,z3))

# vetor Z1 que é a entrada da camada de saída
ones = np.ones((1, Z3.shape[1]))
Z3 = np.vstack((ones, Z3)) # acrescenta uma linha de 1's

# vetor M1 de pesos da camada de saída
aux = np.matmul(y_treino, Z3.transpose())
aux2 = np.linalg.inv(np.matmul(Z3, Z3.transpose()))
M3 = np.matmul(aux, aux2)

# vetor final com os resultados da camasda de saída
y3 = np.matmul(M3,Z3)

#---------------------------------- 4 NEURÔNIOS

# vetor de pesos da camada oculta
W4 = np.random.rand(q4, p+1) * 0.1 # matriz de pesos onde cada elemento varia num intervalo de (0,1) em uma distribuição uniforme

# ativações dos neurônios da camada oculta
u4 = np.matmul(W4, x_treino)

Z4 = np.array([[], [], [], []]) # quatro neurônios

# percorrer todas as N colunas de u
for i in range(0, u4.shape[1]):
    z4 = np.array([[(1 / (1 + (math.exp(-1 * u4[0:1, i:i+1][0][0]))))], [(1 / (1 + (math.exp(-1 * u4[1:2, i:i+1][0][0]))))], [(1 / (1 + (math.exp(-1 * u4[2:3, i:i+1][0][0]))))], [(1 / (1 + (math.exp(-1 * u4[3:4, i:i+1][0][0]))))]])
    Z4 = np.hstack((Z4,z4))

# vetor Z1 que é a entrada da camada de saída
ones = np.ones((1, Z4.shape[1]))
Z4 = np.vstack((ones, Z4)) # acrescenta uma linha de 1's

# vetor M1 de pesos da camada de saída
aux = np.matmul(y_treino, Z4.transpose())
aux2 = np.linalg.inv(np.matmul(Z4, Z4.transpose()))
M4 = np.matmul(aux, aux2)

# vetor final com os resultados da camasda de saída
y4 = np.matmul(M4,Z4)

#---------------------------------- Cálculo de R^2
print('--> Cálculo do coeficiente de determinação \n--> q é o número de neurônios na camada o culta')
# variáveis auxiliares
soma1 = 0
soma2 = 0
media_y = np.mean(y_treino)  # média das amostras

# q = 1
R2_1N = 0
for aux1,aux2 in itertools.zip_longest(y_treino.reshape((2250, 1)), y1.reshape((2250, 1))):
    soma1 += (aux1 - aux2) ** 2
    soma2 += (aux1 - media_y) ** 2
R2_1N = 1 - (soma1 / soma2)
print('q = 1 -> R_2 = %f' % (R2_1N))

# q = 2
for aux1,aux2 in itertools.zip_longest(y_treino.reshape((2250, 1)), y.reshape((2250, 1))):
    soma1 += (aux1 - aux2) ** 2
    soma2 += (aux1 - media_y) ** 2
R2_2N = 1 - (soma1 / soma2)
print('q = 2 -> R_2 = %f' % (R2_2N))

# q = 3
for aux1,aux2 in itertools.zip_longest(y_treino.reshape((2250, 1)), y3.reshape((2250, 1))):
    soma1 += (aux1 - aux2) ** 2
    soma2 += (aux1 - media_y) ** 2
R2_3N = 1 - (soma1 / soma2)
print('q = 3 -> R_2 = %f' % (R2_3N))

# q = 4
for aux1,aux2 in itertools.zip_longest(y_treino.reshape((2250, 1)), y4.reshape((2250, 1))):
    soma1 += (aux1 - aux2) ** 2
    soma2 += (aux1 - media_y) ** 2
R2_4N = 1 - (soma1 / soma2)
print('q = 4 -> R_2 = %f' % (R2_4N))

#---------------------------------- Gráficos

# 1 NEURÔNIO
plt.figure(2)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(data[0:, 0:1], y1.transpose(), color = 'red') # rede neural
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Um neurônio na camada oculta')
plt.grid(True)
# 2 NEURÔNIOS
plt.figure(1)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(data[0:, 0:1], y.transpose(), color = 'red') # rede neural
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Dois neurônios na camada oculta')
plt.grid(True)
# 3 NEURÔNIOS
plt.figure(3)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(data[0:, 0:1], y3.transpose(), color = 'red') # rede neural
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Três neurônios na camada oculta')
plt.grid(True)
# 4 NEURÔNIOS
plt.figure(4)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(data[0:, 0:1], y4.transpose(), color = 'red') # rede neural
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Quatro neurônios na camada oculta')
plt.grid(True)

plt.show()

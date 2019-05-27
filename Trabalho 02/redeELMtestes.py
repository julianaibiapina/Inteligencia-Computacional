import math
import random
import numpy as np
import matplotlib.pyplot as plt
import itertools

data = np.loadtxt('./Trabalho 02/aerogerador.dat')
x_treino = data[0:, 0:1] # velociade do vento
ones = np.ones(x_treino.shape)
x_treino = np.hstack((ones, x_treino)) # acrescenta uma coluna de 1's

y_treino = data[0:, 1:]  # potência
y_treino = y_treino.reshape((1, 2250)) # transforma em um vetor de N colunas

# vetor de pesos da camada oculta
col1 = np.array([[random.uniform(0, 1)], [random.uniform(0, 1)]])
col2 = np.array([[random.uniform(0, 1)], [random.uniform(0, 1)]])
col = np.hstack((col1, col2))
W = np.array(col) # matriz de pesos

# ativações dos neurônios da camada oculta
Z = np.array([[], []])  # define um vetor vazio (2,1)
for i in range(0, x_treino.shape[0]):
    u = np.dot(W, x_treino[i]) # ativação do neurônio i
    z = np.array([[1 / (1 + (math.exp(-1 * u[0])))], [1 / (1 + (math.exp(-1 * u[1])))]])
    Z = np.hstack((Z,z))

# peso do neurônio da camada de saída

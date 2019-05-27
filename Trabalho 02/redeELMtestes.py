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


# vetor de pesos da camada oculta
col1 = np.array([[random.uniform(0, 1)], [random.uniform(0, 1)], [random.uniform(0, 1)]])
col2 = np.array([[random.uniform(0, 1)], [random.uniform(0, 1)], [random.uniform(0, 1)]])
col = np.hstack((col1, col2))
W = np.array(col) # matriz de pesos

#cálculo das ativações dos neurônios da camada oculta

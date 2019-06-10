import math
import random
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


#-------------------------------Definir Centros---------------------------------
data = np.loadtxt('./Trabalho 03/iris_log.dat')

data_centros = data[0:, 0:4]

# Number of clusters
k = 3
# Number of training data
n = data_centros.shape[0]
# Number of features in the data
c = data_centros.shape[1]

# Generate random centers, here we use sigma and mean to ensure it represent the whole data
mean = np.mean(data_centros, axis = 0)
std = np.std(data_centros, axis = 0)
centers = np.random.randn(k,c)*std + mean


centers_old = np.zeros(centers.shape) # to store old centers
centers_new = deepcopy(centers) # Store new centers

clusters = np.zeros(n)
distances = np.zeros((n,k))

error = np.linalg.norm(centers_new - centers_old)

# When, after an update, the estimate of that center stays the same, exit loop
while error != 0:
    # Measure the distance to every center
    for i in range(k):
        distances[:,i] = np.linalg.norm(data_centros - centers_new[i], axis=1)

    # Assign all training data to closest center
    clusters = np.argmin(distances, axis = 1)


    centers_old = deepcopy(centers_new)
    # Calculate mean for every cluster and update the center
    for i in range(k):
        centers_new[i] = np.mean(data_centros[clusters == i], axis=0)
    error = np.linalg.norm(centers_new - centers_old)

# centros encontrados na amostra
t1 = centers_new[0:1, 0:]
t2 = centers_new[1:2, 0:]
t3 = centers_new[2:3, 0:]

# embalhara os dados
data = np.random.permutation(data)
# entradas
x = data[0:, 0:4]
# saídas desejadas
d = data[0:, 4:]

fi1 = list()
fi2 = list()
fi3 = list()

for v in x:
    aux1 = np.linalg.norm(np.subtract(v,t1))
    fi1.append(math.exp(-aux1 ** 2))

    aux2 = np.linalg.norm(np.subtract(v,t2))
    fi2.append(math.exp(-aux2 ** 2))

    aux3 = np.linalg.norm(np.subtract(v,t3))
    fi3.append(math.exp(-aux3 ** 2))


fi1 = np.array(fi1)
fi2 = np.array(fi2)
fi3 = np.array(fi3)


G = np.vstack((fi1, fi2))
G = np.vstack((G, fi3))
ones = np.ones(fi1.shape)
G = np.vstack((G, ones))
G = G.transpose()

# Cálculo da pseudo-inversa da matriz G
aux = np.linalg.inv(np.matmul(G.transpose(), G))
G_mais = np.matmul(aux, G.transpose())

# Cálculo de w, o vetor de pesos da cadada de saída
w = np.matmul(G_mais, d)
print(w)

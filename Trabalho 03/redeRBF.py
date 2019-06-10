import math
import random
import numpy as np


#centros
t1 = np.array([1, 1])
t2 = np.array([0, 0])

# entradas
x = np.array([[1,1], [0, 1], [0, 0], [1, 0]])
# saída desejada
d = np.array([0, 1, 0, 1])


fi1 = list()
fi2 = list()
for v in x:
    aux1 = np.linalg.norm(np.subtract(v,t1))
    fi1.append(math.exp(-aux1 ** 2))
    aux2 = np.linalg.norm(np.subtract(v,t2))
    fi2.append(math.exp(-aux2 ** 2))
fi1 = np.array(fi1)
fi2 = np.array(fi2)


G = np.vstack((fi1, fi2))
ones = np.ones(fi1.shape)
G = np.vstack((G, ones))
G = G.transpose()

# Cálculo da pseudo-inversa da matrig G
aux = np.linalg.inv(np.matmul(G.transpose(), G))
G_mais = np.matmul(aux, G.transpose())

# Cálculo de w, o vetor de pesos da cadada de saída
w = np.matmul(G_mais, d)
print(w)

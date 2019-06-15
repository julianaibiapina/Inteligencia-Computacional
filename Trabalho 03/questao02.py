import math
import random
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from statistics import mean

data = np.loadtxt('./Trabalho 03/iris_log.dat')

#-------------------------------Definir Centros---------------------------------
data_centros = data[0:, 0:4]

# Número de clusters
k = 3
# Número de dados para treino
n = data_centros.shape[0]
# Número de variáveis
c = data_centros.shape[1]


# Encontra três pontos aleatórios dentro do conjunto de dados para serem os centros iniciais
centers = np.empty((k,c))
for i in range(0,k):
    centers[i] = data_centros[random.randint(0,n-1)]


centers_old = np.zeros(centers.shape) # armazena os centros antigos
centers_new = deepcopy(centers) # guarda os novos centros

clusters = np.zeros(n)
distances = np.zeros((n,k))

error = np.linalg.norm(centers_new - centers_old)

# quando ocenters_new == centers_old então sai do loop
while error != 0:
    # Calcula a distância para cada centro
    for i in range(k):
        distances[:,i] = np.linalg.norm(data_centros - centers_new[i], axis=1)


    # associa cada dado de treinamento ao centro mais próximo dele
    clusters = np.argmin(distances, axis = 1)


    centers_old = deepcopy(centers_new)
    # Calcula a média para cada cluster e atualiza os seus respectivos centros
    for i in range(k):
        centers_new[i] = np.mean(data_centros[clusters == i], axis=0)
    error = np.linalg.norm(centers_new - centers_old)

# centros encontrados na amostra
t1 = centers_new[0:1, 0:]
t2 = centers_new[1:2, 0:]
t3 = centers_new[2:3, 0:]


# ----------------------RBF-----------------------------------------------------
# variável para calcular a média de acertos
media = list()
for j in range(0, 50):

    data = np.random.permutation(data) # embalhara os dados
    data_treino = data[0:120, 0:]      # dados de treino
    data_teste = data[120:, 0:]        # dados de teste

    # entradas
    x = data_treino[0:, 0:4]
    # saídas desejadas
    d = data_treino[0:, 4:]

    # ----------------------------------TREINO--------------------------------------
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

    # cálculo da matriz G
    G = np.vstack((fi1, fi2))
    G = np.vstack((G, fi3))
    ones = np.ones(fi1.shape)
    G = np.vstack((G, ones))
    G = G.transpose()


    # Cálculo da pseudo-inversa da matriz G: G_mais
    aux = np.linalg.inv(np.matmul(G.transpose(), G))
    G_mais = np.matmul(aux, G.transpose())

    # Cálculo de w, o vetor de pesos da camada de saída
    w = np.matmul(G_mais, d)

    # y = np.matmul(G, w)

    # ----------------------------------TESTE---------------------------------------

    # entradas
    x_teste = data_teste[0:, 0:4]

    # saídas esperadas
    d_teste = data_teste[0:, 4:]

    fi1_t = list()
    fi2_t = list()
    fi3_t = list()

    for v in x_teste:
        aux1 = np.linalg.norm(np.subtract(v,t1))
        fi1_t.append(math.exp(-aux1 ** 2))

        aux2 = np.linalg.norm(np.subtract(v,t2))
        fi2_t.append(math.exp(-aux2 ** 2))

        aux3 = np.linalg.norm(np.subtract(v,t3))
        fi3_t.append(math.exp(-aux3 ** 2))


    fi1_t = np.array(fi1_t)
    fi2_t = np.array(fi2_t)
    fi3_t = np.array(fi3_t)

    # cálculo da matriz G
    G_teste = np.vstack((fi1_t, fi2_t))
    G_teste = np.vstack((G_teste, fi3_t))
    ones = np.ones(fi1_t.shape)
    G_teste = np.vstack((G_teste, ones))
    G_teste = G_teste.transpose()

    y = np.matmul(G_teste, w)
    resultado_rede = np.argmax(y, axis=1)
    resultado_esperado = np.argmax(d_teste, axis=1)

    # achar a porcentagem de acerto
    cont = 0
    for i in range(0, resultado_rede.shape[0]):
        if resultado_rede[i] == resultado_esperado[i]:
            cont += 1
    # transforma resultado em porcentagem
    cont = cont / d_teste.shape[0]
    media.append(cont)
    #print('Porcentagem de acertos: %8.4f %%' % (cont))

print('Média de acertos: %8.3f %% \nValor máximo: %8.3f %% \nValor mínimo: %8.3f %%'%  (mean(media), max(media), min(media)))

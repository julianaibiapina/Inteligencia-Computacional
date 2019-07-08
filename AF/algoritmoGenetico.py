import math
import random
import numpy as np


def f(x, y):
    return (1 - x)**2 + 100*(y - x**2)**2

# população
populacao = 100

# termos iniciais da busca em binário
x_b = np.random.randint(0, 2, (populacao,8))
y_b = np.random.randint(0, 2, (populacao,8))

individuos = np.hstack((x_b,y_b))

# pais em binário
pais = np.zeros(individuos.shape)

# vetor avaliação dos indivíduos
notas = np.zeros((populacao,1))

# limite e contador de épocas
geracoes = 100
cont = 0


while(cont<geracoes):
    # binário para decimal
    x = np.packbits(individuos[:, 0:8], axis=-1)
    # Normalização binário para intervalo -5 a 5
    x = np.multiply(x,10/255)-5
    y = np.packbits(individuos[:, 8:], axis=-1)
    y = np.multiply(y,10/255)-5

    #coloca notas em toda a população no vetor notas e soma um para tds os indivíduos terem chances
    for i in range(0, populacao):
        notas[i] = (1/(f(x[i][0],y[i][0])+1))

    # roleta

    total = np.sum(notas)
    #percorre população
    for i in range(0, populacao):
        aux1 = 0
        # nota do primeiro elemento
        aux2 = notas[aux1]

        # valor aleatório entre o intervalo de soma de todas as notas
        a = np.random.uniform(0,1,1)*total
        
        # pega o individuo q está nessa posição e o torna pai
        while aux2 < a:
            aux1 += 1
            aux2 += notas[aux1]
        
        pais[i, :] = individuos[aux1, :]


    # Crossover

    #ponto de corte
    corte = np.random.randint(1, 15, 1)
    #print(corte[0])
    # Cruzamento
    for i in range(0, populacao, 2):
        individuos[i, :] = np.hstack((pais[i, 0:corte[0]],pais[i+1, corte[0]:]))
        individuos[i+1, :] = np.hstack((pais[i+1, 0:corte[0]],pais[i, corte[0]:]))

    # acrescenta contagem de épocas
    cont += 1
print('fim')

#Verificação dos individuos finais
x = np.packbits(individuos[:, 0:8], axis=-1)
x = np.multiply(x,10/255)-5
y = np.packbits(individuos[:, 8:], axis=-1)
y = np.multiply(y,10/255)-5


for i in range(0, populacao):
    notas[i] = f(x[i][0], y[i][0])

print(notas)

#Função que encontra a posição que está a menor nota.
pos = list(notas).index(min(notas))

print(pos)

#inviduo (x e y) daquela posição
xpos = x[pos][0]
ypos = y[pos][0]

#Valor de x e y que foi encontrado o mínimo
print(xpos)
print(ypos)

#minímo encontrado
print(f(xpos,ypos))


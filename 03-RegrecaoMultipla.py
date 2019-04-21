import numpy as np
import matplotlib.pyplot as plt
import itertools

data = np.loadtxt('aerogerador.dat')

x = data[0:, 0:1] # velociade do vento
y = data[0:, 1:]  # potência

B_0 = 0
B_1 = 0

# Cálculo de B_1
t1 = 0 # somatório de x*y
n = 0  # número total de amostras
t2 = 0 # somatório de y
t3 = 0 # somatório de x
t4 = 0 # somatório de x**2

for aux1,aux2 in itertools.zip_longest(x,y):
    t1 = t1 + (aux1 * aux2)
    n += 1
    t2 = t2 + aux2
    t3 = t3 + aux1
    t4 = t4 + (aux1 ** 2)

B_1 = (t1 - ((1 / n) * t2 * t3) ) / (t4 - ((1 / n) * (t3 ** 2)))
print('B_1 = %8.3f' % (B_1))

# Cálculo de B_0
media_y = (t2 / n)
media_x = t3



#Exibe a disperção dos dados num gráfico (x,y)
plt.scatter(data[0:, 0:1], data[0:, 1:])
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
#plt.show()

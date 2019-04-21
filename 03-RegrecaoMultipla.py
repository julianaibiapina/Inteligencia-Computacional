import numpy as np
import matplotlib.pyplot as plt
import itertools

data = np.loadtxt('aerogerador.dat')

x = data[0:, 0:1] # velociade do vento
y = data[0:, 1:]  # potência

B_0 = 0
B_1 = 0

# B_0
# termo 1
t1 = 0
n = 0
t2 = 0

for aux1,aux2 in itertools.zip_longest(x,y):
    t1 = t1 + (aux1 * aux2)
    n += 1
    t2 = t2 + aux2
    #print("pot x velo: %8.3f  %8.3f, %s" % (aux1,aux2, type(aux1)))
    print("t1 =  %8.3f \nn = %d \nt2 = %8.3f" % (t1, n, t2))

#Exibe a disperção dos dados num gráfico (x,y)
plt.scatter(data[0:, 0:1], data[0:, 1:])
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.show()

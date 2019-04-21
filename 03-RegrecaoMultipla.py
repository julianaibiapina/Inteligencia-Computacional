import numpy as np
import matplotlib.pyplot as plt
import itertools

data = np.loadtxt('aerogerador.dat')

x = data[0:, 0:1] # velociade do vento
y = data[0:, 1:]  # potência

# REGRESSÃO LINEAR
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


# Cálculo de B_0
media_y = t2 / n
media_x = t3 / n
B_0 = media_y - (B_1 * media_x)

print('B_0 = %8.3f' % (B_0))
print('B_1 = %8.3f' % (B_1))

list_linhas = list()
list_matrix = list()
new_value = 0

for aux in x:
    new_value = B_0 + (B_1 * aux[0])
    list_linhas = [aux[0], new_value[0]]
    list_matrix.append(list_linhas)


teste = np.array(list_matrix)
#print(teste)
#print(data)

# Cálculo de R^2
R_2 = 0
soma1 = 0
soma2 = 0
for aux1,aux2 in itertools.zip_longest(y, teste[0:, 1:]):
    soma1 += (aux1 - aux2) ** 2
    soma2 += (aux1 - media_y) ** 2
R_2 = 1 - (soma1 / soma2)
print('R_2 = %8.3f' % (R_2))




#Exibe a disperção dos dados num gráfico (x,y)
# plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(teste[0:, 0:1], teste[0:, 1:], color = 'yellow') # regressão
# plt.ylabel('Potência')
# plt.xlabel('Velocidade do Vento')
# plt.show()

# REGRESSÃO MÚLTIPLA

# Cria as matrizes X's, cujos valores são [x, x^2], [x, x^2, x^3], [x, x^2, x^3, x^4] e [x, x^2, x^3, x^4, x^5]

list_linhas = list()
list_matrix1 = list()
list_matrix2 = list()
list_matrix3 = list()
list_matrix4 = list()

x_2 = 0
x_3 = 0
x_4 = 0
x_5 = 0

for aux in x:
    x_2 = aux[0] ** 2
    x_3 = aux[0] ** 3
    x_4 = aux[0] ** 4
    x_5 = aux[0] ** 5

    # Para matrix X1 - polinômio de grau dois
    list_linhas = [1, aux[0], x_2]
    list_matrix1.append(list_linhas)

    # Para matrix X2 - polinômio de grau três
    list_linhas = [1, aux[0], x_2, x_3]
    list_matrix2.append(list_linhas)

    # Para matrix X3 - polinômio de grau quatro
    list_linhas = [1, aux[0], x_2, x_3, x_4]
    list_matrix3.append(list_linhas)

    # Para matrix X4 - polinômio de grau cinco
    list_linhas = [1, aux[0], x_2, x_3, x_4, x_5]
    list_matrix4.append(list_linhas)


matrix_y = np.matrix(y)
matrix1 = np.matrix(list_matrix1) # Matriz X1 para polinômio de grau 2
matrix2 = np.matrix(list_matrix2) # Matriz X2 para polinômio de grau 3
matrix3 = np.matrix(list_matrix3) # Matriz X3 para polinômio de grau 4
matrix4 = np.matrix(list_matrix4) # Matriz X4 para polinômio de grau 5


# Regressão polinomial de grau 2
x_transposta = matrix1.transpose()
mult = np.matmul(x_transposta, matrix1)
inversa_mult =  np.linalg.inv(mult)
intermediario = np.matmul(inversa_mult, x_transposta)
B_poli2 = np.matmul(intermediario, y)

# Resultado da regressão polinomial de ordem dois
y_poli2 = np.matmul(matrix1, B_poli2)
print(y_poli2[0:,0:1])
print(matrix1[0:, 1:2])


#Exibe a disperção dos dados num gráfico (x,y)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(matrix1[0:, 1:2], y_poli2[0:,0:1], color='magenta')  # regressão
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.show()

# Autor: Juliana Franco Ibiapina
# Inteligênica Computacional - 2019.1

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
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


list_linhas = list()
list_matrix = list()
new_value = 0

for aux in x:
    new_value = B_0 + (B_1 * aux[0])
    list_linhas = [aux[0], new_value[0]]
    list_matrix.append(list_linhas)


teste = np.array(list_matrix)



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
# Resultado da regressão polinomial de grau dois
B_poli2 = np.matmul(intermediario, y)
y_poli2 = np.matmul(matrix1, B_poli2)


# Regressão polinomial de grau três
x_transposta = matrix2.transpose()
mult = np.matmul(x_transposta, matrix2)
inversa_mult = np.linalg.inv(mult)
intermediario = np.matmul(inversa_mult, x_transposta)
# Resultado da regressão polinomial de grau três
B_poli3 = np.matmul(intermediario, y)
y_poli3 = np.matmul(matrix2, B_poli3)


# Regressão polinomial de grau quatro
x_transposta = matrix3.transpose()
mult = np.matmul(x_transposta, matrix3)
inversa_mult = np.linalg.inv(mult)
intermediario = np.matmul(inversa_mult, x_transposta)
# Resultado da regressão polinomial de grau quatro
B_poli4 = np.matmul(intermediario, y)
y_poli4 = np.matmul(matrix3, B_poli4)


# Regressão polinomial de grau cinco
x_transposta = matrix4.transpose()
mult = np.matmul(x_transposta, matrix4)
inversa_mult = np.linalg.inv(mult)
intermediario = np.matmul(inversa_mult, x_transposta)
# Resultado da regressão polinomial de grau cinco
B_poli5 = np.matmul(intermediario, y)
y_poli5 = np.matmul(matrix4, B_poli5)


# Cálculo de R^2
print('--> Cálculo do coeficiente de determinação e do coeficiente de determinação ajustado')

# variáveis auxiliares
soma1 = 0
soma2 = 0

# regressão linear
R_2_linear = 0
for aux1,aux2 in itertools.zip_longest(y, teste[0:, 1:]):
    soma1 += (aux1 - aux2) ** 2
    soma2 += (aux1 - media_y) ** 2
R_2_linear = 1 - (soma1 / soma2)
print('Regressão Linear \n  R_2 = %f' % (R_2_linear))

# regressão polinomial grau 2
R_2_grau2 = 0
soma1 = 0 # reinicia as variáveis
soma2 = 0
for aux1,aux2 in itertools.zip_longest(y, y_poli2):
    soma1 += (aux1 - aux2) ** 2
    soma2 += (aux1 - media_y) ** 2
R_2_grau2 = 1 - (soma1 / soma2)
R_2_grau2_ajustado = 1 - ((soma1 / (n - 3) ) / (soma2 / (n - 1))) # k = 2
print('Regressão Polinomial de grau 2 \n  R_2 = %f \n  R_2_ajustado = %f' % (R_2_grau2, R_2_grau2_ajustado))

# regressão polinomial grau 3
R_2_grau3 = 0
soma1 = 0 # reinicia as variáveis
soma2 = 0
for aux1,aux2 in itertools.zip_longest(y, y_poli3):
    soma1 += (aux1 - aux2) ** 2
    soma2 += (aux1 - media_y) ** 2
R_2_grau3 = 1 - (soma1 / soma2)
R_2_grau3_ajustado = 1 - ((soma1 / (n - 4) ) / (soma2 / (n - 1))) # k = 3
print('Regressão Polinomial de grau 3 \n  R_2 = %f \n  R_2_ajustado = %f' % (R_2_grau3, R_2_grau3_ajustado))

# regressão polinomial grau 4
R_2_grau4 = 0
soma1 = 0 # reinicia as variáveis
soma2 = 0
for aux1,aux2 in itertools.zip_longest(y, y_poli4):
    soma1 += (aux1 - aux2) ** 2
    soma2 += (aux1 - media_y) ** 2
R_2_grau4 = 1 - (soma1 / soma2)
R_2_grau4_ajustado = 1 - ((soma1 / (n - 5) ) / (soma2 / (n - 1))) # k = 4
print('Regressão Polinomial de grau 4 \n  R_2 = %f \n  R_2_ajustado = %f' % (R_2_grau4, R_2_grau4_ajustado))

# regressão polinomial grau 5
R_2_grau5 = 0
soma1 = 0 # reinicia as variáveis
soma2 = 0
for aux1,aux2 in itertools.zip_longest(y, y_poli5):
    soma1 += (aux1 - aux2) ** 2
    soma2 += (aux1 - media_y) ** 2
R_2_grau5 = 1 - (soma1 / soma2)
R_2_grau5_ajustado = 1 - ((soma1 / (n - 6) ) / (soma2 / (n - 1))) # k = 5
print('Regressão Polinomial de grau 5 \n  R_2 = %f \n  R_2_ajustado = %f' % (R_2_grau5, R_2_grau5_ajustado))




#Exibe os dados num gráfico (x,y)

# Linear
plt.figure(1)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(teste[0:, 0:1], teste[0:, 1:], color = 'red') # regressão linear
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Regressão Linear')
plt.grid(True)

# Polinomial grau 2
plt.figure(2)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(matrix1[0:, 1:2], y_poli2[0:,0:1], color='red')  # regressão polinomial grau 2
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Regressão Polinomial de Grau 2')
plt.grid(True)

# Polinomial grau 3
plt.figure(3)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(matrix2[0:, 1:2], y_poli3[0:,0:1], color='red')  # regressão polinomial grau 3
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Regressão Polinomial de Grau 3')
plt.grid(True)

# Polinomial grau 4
plt.figure(4)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(matrix3[0:, 1:2], y_poli4[0:,0:1], color='red')  # regressão polinomial grau 4
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Regressão Polinomial de Grau 4')
plt.grid(True)

# Polinomial grau 5
plt.figure(5)
plt.scatter(data[0:, 0:1], data[0:, 1:])   # amostras
plt.plot(matrix4[0:, 1:2], y_poli5[0:,0:1], color='red')  # regressão polinomial grau 5
plt.ylabel('Potência')
plt.xlabel('Velocidade do Vento')
plt.title('Regressão Polinomial de Grau 5')
plt.grid(True)

plt.show()

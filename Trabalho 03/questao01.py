import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#------------------------GRÁFICO------------------------
data = np.loadtxt('./Trabalho 03/twomoons.dat')
x_1 = data[0:, 0:1]
x_2 = data[0:, 1:2]
rotulo = data[0:, 2:3]
# CLASSE A = 0:501
# CLASSE B = 501:
# CLASSE A
ax.scatter(x_1[0:501], x_2[0:501], rotulo[0:501], c='r', marker='o')
# CLASSE A
ax.scatter(x_1[501:], x_2[501:], rotulo[501:], c='b', marker='^')

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('Rótulo')
plt.show()

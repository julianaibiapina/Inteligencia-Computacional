#https://www.kaggle.com/andyxie/k-means-clustering-implementation-in-python

import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Set three centers, the model should predict similar results
center_1 = np.array([1,1])
center_2 = np.array([5,5])
center_3 = np.array([8,1])

# Generate random data and center it to the three centers
data_1 = np.random.randn(200, 2) + center_1
data_2 = np.random.randn(200,2) + center_2
data_3 = np.random.randn(200,2) + center_3

data = np.concatenate((data_1, data_2, data_3), axis = 0)


plt.scatter(data[:,0], data[:,1], s=7)
plt.show()

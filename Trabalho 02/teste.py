import numpy as np
A = np.array([1, 1, 0, 0])
A = A.reshape((1,4))
B = np.array([[1], [2], [3], [4]])

M = np.matmul(B, A)
print(M)

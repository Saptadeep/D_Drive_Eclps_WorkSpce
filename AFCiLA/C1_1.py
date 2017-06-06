import numpy as np

a = np.array([[2,3],[1,-1]])
b = np.array([-8,6])
x=np.linalg.solve(a, b)
print x
np.allclose(np.dot(a, x), b)
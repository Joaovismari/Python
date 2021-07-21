import numpy as np

a= np.array([[1,1,1],[1,2,2],[2,1,3]])
b = np.array([6,9,11])
print(np.linalg.solve(a,b))
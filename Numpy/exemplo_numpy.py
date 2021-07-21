import numpy as np

a_1 = np.array([[1, 1, 1], [4, 5, 6]])  # 1 colchete = linhas, 2 colchetes = colunas
print(a_1.shape)  # a forma possui 2 linhas e 3 colunas
print(a_1.size)  # numero de elementos/celulas no array
print(a_1.ndim)  # numero de dimenssões
print(a_1.dtype)  # tipo de dados do array, o array só aceita 1 tipo de dado

a_2 = np.arange(27).reshape(3,3,3)#passa um numero de elementos e redistribui em arrays de 3 dimenssões
print(a_2)

a= np.sin(np.pi/2)
print(a)
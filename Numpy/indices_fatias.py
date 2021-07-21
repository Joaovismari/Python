import numpy as np

a = np.arange(10)**2
print(a[:2])#retorna os elementos anteriores à posição 2
print(a[2:])#retorna os elementos sucessores à posição 2
print(a[::2])#retorna os elementos pelo intervalo de posição de 2 em 2
print(a[::-2])#retorna os elementos pelo intervalo de posição de 2 em 2 em sentido decrescente
print(a[2:8:2])#retorna os elementos pelo intervalo de posição inicio, fim,passo entre o inicio e fim

b = np.arange(20).reshape(4,5)
print(b)#array redimensionado
print(b[1])#retorna um sub array referente a linha do array
print(b[1,2])#elemento linha 1, coluna 2, valor = 7
print(b[1,2:])#elemento linha 1, coluna 2 em diante
print(b[2:,3:])#elemento linha 2 em diante, coluna 2 em diante, retorna submatriz

c = np.arange(27).reshape(3,3,3)#array 3D
print(c)
print(c[1,2,0])#dimensao 1, linha 2,coluna 0 = 15

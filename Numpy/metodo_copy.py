import numpy as np

a = np.arange(8)#criado array com 8 posições de 0 à 7
print(a)
b = a#caso haja alteração à mesma é copiada
a[0]=9#alteração
print(b)
c= a.copy()#feita copia do array em seu estado até então de maneira imutavel
print(c)
a[1]=3#modificado
print(a)#com modificação
print(c)
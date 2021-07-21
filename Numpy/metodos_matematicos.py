import numpy as np

my_array = np.arange(8).reshape(2,4)**2
my_array[0][0] =11
print('my array',my_array)

print(my_array.max())#valor maximo do array
print(my_array.min(axis=1))#argumento por linha,eixo, valor minimo
print(my_array.argmin())#menor indice
print(my_array.argmax())#maior indice
print(my_array.sum())#soma dos valores armazenado no array
print(my_array.mean())#media dos valores armazenados
print(my_array.cumsum())#soma acumulada em array
print(my_array.std())#desvio padrão

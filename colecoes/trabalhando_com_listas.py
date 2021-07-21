lista_quadrados = []

for i in range(5):
    lista_quadrados.append(i**2)
print(lista_quadrados)


a = list(range(10))
print(a)

numeros = [1,2,3,4,5,7]
f = lambda x:x**2 #isso é igual à def f(x): x**2

lista_5 = list(map(f,numeros))#criando um map com os quadrados da list numeros
print(lista_5)

quadrados = [x**2 for x in range(7)]
print(quadrados)
#exercicio 1

lista = ['P', 'A', 'Y', 'A', 'T', 'A', 'H', 'O', 'N']
n = lista.count('A')
for i in range(n):
    lista.remove('A')

print('elementos: ',n,', nova lista:',lista)

#exercicio 2
lista_impar = [(i * 2+1) for i in range(26)] #funcional
print(lista_impar)

f_x = lambda x:(x*2+1) #com lambda
impares = [f_x(x) for x in range(26)]
print(impares)

#exercicio 3

valores = [1,2,3,4,5]
keys = ['a','b','c','d','e']
dicionario = {}
for i in range(len(valores)):
    dicionario[keys[i]]=valores[i]

print(dicionario.items())

#exercicio 4
keys = list(dicionario.keys())
valores = list(dicionario.values())
print(keys)
print(valores)
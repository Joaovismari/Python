print("Resumo introdução à python")

j = 1
nome = 'João'
sobrenome = "Vismari de Lacerda"
pi = 3.14
mensagem = 'string no Python'

nc =nome+" "+sobrenome #concatenação
print(nome.upper())#converte pra maiuscula
print(sobrenome.lower())#converte pra minuscula
print(nome[2])#captura o caractere pelo seu indice
print(nome[0:3])#captura os caracteres pelo indice entre as posições 0 e 3
print(nome[-4]) #captura o caractere pelo indice do fim para o começo
print(len(nome)) #comprimento de uma String
print(type(pi))#retorna o tipo da variavel
if j == True:# condicional simples comparando booleano a 1
    print('Verdadeiro')
else:
    print("falso")

nome_1 = 'Mila'
nome_2 = 'Mila'

if nome_1 is nome_2: # is compara o endereço de memoria
    print('iguais')
else:
    print('diferentes')

print(mensagem.find('Python'))# retorna a posição aonde o parametro foi encontrado no caso a partir do indice 10
nova_mensagem = mensagem.replace('Python', 'Java')#substitui passando dois parametros atual e novo
print(nova_mensagem)

lista_mensagem = mensagem.split(' ')#cria uma lista com o criterio de separação à partir do parametro passado
print(lista_mensagem)
print(lista_mensagem[2])#retorna o elemento armazenado no indice buscado
print(type(lista_mensagem))#tipo lista
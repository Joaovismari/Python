#Listas

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(type(programadores)) # type ‘list’
print(len(programadores)) # 5
print(programadores[4]) # Luana

programadores.remove('Samuel')# remove Elemento pelo valor passado
programadores.pop(2)# remove elemento pela posição passada

programadores.append('João') #adiciona elemento na ultima posição da lista
programadores.insert(0,'Kratos')#adiciona elemento passando indice aonde será armazenado na lista
print(programadores)
programadores.sort() #organiza em ordem crescente
print(programadores)
programadores.reverse() #organiza em ordem decrescente
print(programadores)

aluno=['João', 28, 1.81] #podem ter tipos diferentes de dados na mesma lista
print(aluno)
aluno.clear() # remove todos os elementos de uma lista
print(aluno)
aluno.append('j')
aluno.append('j')
aluno.append('k')
aluno.append('j')
print(aluno.count('j')) #contabiliza o numero de vezes que o elemento passado aparece na lista
print(aluno.index('j')) #devolve indice aonde o elemento aparece a primeira vez na lista
print(aluno.index('j',2)) #devolve indice aonde o elemento aparece a primeira vez após o indice passado '2'


#programadores.pop(12) Erro ao remover uma posição inexistente IndexError

numeros = [15, 5, 0, 20, 10]
nomes = ['Caio', 'Alex', 'Renata', 'Patrícia', 'Bruno']

print(min(numeros)) # 0
print(max(numeros)) # 20
print(min(nomes)) # Alex
print(max(nomes)) # Renata
print(sum(numeros)) #soma elementos de uma lista
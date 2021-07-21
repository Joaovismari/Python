import numpy as np

a_4 = np.ones(6)*11#preenche array com um's,
print('a_4\n',a_4)

a_5 = np.eye(4)#retorna matriz identidade
print('a_5\n',a_5)

a_6 = np.arange(0,10,0.5)#parametros de contagem inicio,fim,passo de soma do inicio ao fim
print('a_6\n',a_6)

a_7 = np.linspace(0,10,12)#parametros de contagem inicio,fim,numero de divisoes no caso 12
print('a_7\n',a_7)

a_8 = np.ones(8)
a_8.reshape(2,4)#redimensiona o array anterior que era 8 colunas em
print('a_8\n',a_8)#2 linhas e 4 colunas, alteração não permanece

a_9 = np.ones(8)
a_9.resize(2,4)#modifica o array anterior que era 8 colunas em
print('a_9\n',a_9)#2 linhas e 4 colunas, alteração é fixa

a_10 = np.zeros(8)
a_10.resize(2,4)#modificado
print('a_10\n',a_10)

a_11 = np.vstack((a_9,a_10))#adiciona os elementos de um array na vertical
print('a_11\n',a_11)

a_12 = np.hstack((a_9,a_10))# adiciona os elementos de um array na horizontal
print('a_12\n', a_12)

a_13 = np.vstack((a_11,a_9))# tendo o mesmo numero de linhas e colunas não há limitações
print('a_13\n',a_13)
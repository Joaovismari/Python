import pandas as pd
import  numpy as np

# Dados
lista_a = [11,22,33,44,55]
lista_b = ['a','b','c','d','e']

arr = np.arange(10)**2#array com numpy

dic = {'coluna1':np.arange(10)*5,'coluna2':np.arange(10)**2,'coluna3':np.ones(10)}
#print(dic)#dic  estruturado, 3 colunas cada qual com seu array gerado pelo numpy

serie_1 = pd.Series(lista_b,index=lista_a)#estrutura series dados,indices
#print(serie_1)# similar à array

serie_3 = pd.Series(arr)#criação de serie com array numpy indice automatico
#print(serie_3)

df1 = pd.DataFrame(dic) #estrutura  'dataframe' utilizando um array estruturado com 'n'
#print(df1) #dimensões

arr2 = np.arange(15).reshape(5,3)#5 colunas, 3 linhas
df3 = pd.DataFrame(arr2)#dataframe criado com array numpy
print(df3)
import pandas as pd
import numpy as np


lista_a = ['a','a','b','c','a','d','c']
lista_b = list(range(7))

dic = {'strings':lista_a,'numeros':lista_b}

df = pd.DataFrame(dic)#cria um dataframe
#print(df.values)# valores do dataframe sem os indices
#print(type(df.values))#tipo dos valores armazenados
#print(list(df.columns))#extrai as colunas do dataframe em formato de lista
#print(list(df.index))#extrai os indices do dataframe em formato de lista
#print(df.shape)#mostra o formato do dataframe em linhas, colunas

df2 = pd.DataFrame({'col1':np.arange(100)**2,'col2':np.arange(100)*5})
print(df2.head())#mostra o inicio do dataframe 5 primeiros resultados
print(df2.tail())#mostra o fim do dataframe 5 ultimos resultados
print(df.cumsum())#soma cumulativa do dataframe
print(df2.sum())#soma valor total do dataframe por coluna
print(df2.mean())#media de valores do dataframe por coluna
print(df['strings'].value_counts())#conta o numero de vezes que um valor se repete numa serie dentro de um dataframe
print(df.sort_values(by='strings'))#ordena os valores por uma coluna ordem alfabetica
print(df2.max())#valores maximos do dataframe
print(df2.min())#valores minimos do dataframe
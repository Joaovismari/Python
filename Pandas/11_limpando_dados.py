import numpy as np
import pandas as pd

a_arr = np.arange(20).reshape(4,5)
df_columns=['A','B','C','D','E']

a_df = pd.DataFrame(a_arr,columns=df_columns)
#print(a_df.drop(2))#remove a linha 2,(padrão primeiro arg é index)
#print(a_df.drop([0,2]))#remove as linha 0 e 2
#print(a_df.drop(columns='C'))#remove a coluna C

b_arr = np.vstack([a_arr,np.array([np.nan,np.nan,np.nan,np.nan,np.nan])])
#print(b_arr)#agrupado na vertical
b_df = pd.DataFrame(b_arr,columns=df_columns)
#print(b_df.isnull())#boleano se vazio
#print(b_df.notnull())#boleano se preenchido
#print(b_df[b_df['A'].notnull()])#filtro apenas valores não nulos
#print(b_df[b_df['A'].isnull()])#filtro apenas valores  nulos

c_arr = np.vstack([a_arr,np.array([np.nan,2,np.nan,np.nan,np.nan])])
c_df = pd.DataFrame(c_arr,columns=df_columns)
#print(c_df.dropna())#remove as linhas que possuem valores nulos, how = any
#print(c_df.dropna(how='all'))#somente se todos os valores forem nulos
#print(c_df.fillna(value=99))#preenche os valores, nulos#

d_arr = np.vstack([a_arr,np.array([15,16,17,18,19])])
d_df = pd.DataFrame(d_arr,columns=df_columns)
print(d_df.duplicated(keep='first'))#mantem apenas a primeira ocorrência, acusando as demais
print(d_df.duplicated(keep='last'))#mantem apenas a ultima ocorrência, acusando as demais
print(d_df.duplicated(subset='A'))#analisa apenas a coluna selecionada
print(d_df.drop_duplicates())#remove linhas duplicadas
print(d_df.drop_duplicates(subset='A'))#remove linhas duplicadas com valores da coluna A repetidos
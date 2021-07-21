import pandas as pd

desired_width=600
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',27)


df = pd.read_csv('horarios.csv',sep=';', engine='python')

df['time'] = pd.to_datetime(df['horario'])#cria coluna time com valor convertido
#print(df['time'][1])#exibe primero resultado de time já como timeStamp

filtro_2 = df['razao_social'].value_counts() == 2

#print(filtro_2[filtro_2])#apenas valores true
lista_filtrada = list(filtro_2[filtro_2].index) # filtro pergunta 1
tabela_filtrada = df[df['razao_social'].isin(lista_filtrada)] #filtro serie com valores booleanos
#print(tabela_filtrada)#resposta pergunta 1

pivot = pd.pivot_table(tabela_filtrada,index='razao_social',values='time',aggfunc=['min','max'])
pivot['total_time']= pivot[('max', 'time')] - pivot[('min', 'time')]






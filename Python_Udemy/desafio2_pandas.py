# coding: utf-8
import pandas as pd

file_path = 'PIB_100_maiores_cidades_2017.txt'

df = pd.read_csv(file_path, engine='python')  # dataframe
df.head()

contador_estados = df['Estado'].value_counts()

Is_sp = df['Estado'] == 'SP'
df_sp = df[Is_sp]
df_sp.head()

print(df_sp)

pib_sp = df_sp['Participação (%)'].sum()
print(pib_sp)

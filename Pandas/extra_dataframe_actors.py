import pandas as pd

#configurações para visualização de dataframes com mais de 5 colunas no pycharm
desired_width=420
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',20)
#np.set_printoption(linewidth=desired_width) caso seja necessario utilizar o numpy

file = 'Oscars.csv'

df = pd.read_csv(file)
df2 = df.loc[::, 'movie' : 'person']
print(df.columns)
print(df.loc[0:2, 'movie' : 'person'])

print(df2['person'].value_counts().head())#atores mais premiados
print(df2['movie'].value_counts().head())#filmes mais premiados


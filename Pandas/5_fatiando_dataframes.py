import pandas as pd

#configurações para visualização de dataframes com mais de 5 colunas no pycharm
desired_width=420
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',20)
#np.set_printoption(linewidth=desired_width) caso seja necessario utilizar o numpy

file = 'datasets_1358_30676_Players.csv'

df = pd.read_csv(file)
df.rename(columns={'Unnamed: 0':'id'},inplace=True)#renomeando uma coluna Unnamed
print(df.loc[1:4,'height':'birth_state'])#fatiando pelos nomes de linhas e colunas como indices
print(df.iloc[1:4,0:2])#fatiando pelos numeros das linhas e colunas como indices
print(df.iloc[0:10:2,0:2])#retornando os resultados de 2 em 2



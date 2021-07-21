import pandas as pd

#configurações para visualização de dataframes com mais de 5 colunas no pycharm
desired_width=420
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',20)
#np.set_printoption(linewidth=desired_width) caso seja necessario utilizar o numpy

file = 'datasets_1358_30676_Players.csv'

df = pd.read_csv(file)
df.rename(columns={'Unnamed: 0':'id'},inplace=True)#renomeando uma coluna Unnamed

from_california = df['birth_state'] == 'California' #cria-se uma marcação booleana

after_1970 = df['born'] > 1970 # operações matematicas

print(df[from_california].head())#essa marcação é usada como filtro/indice
print(df[after_1970])#essa marcação é usada como filtro/indice

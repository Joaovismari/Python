import pandas as pd

file = 'datasets_1358_30676_Players.csv'

df = pd.read_csv(file)

print('Altura média dos jogadores:', round(df['height'].mean(), 2))  # round para arrendondar com 2 casas decimais
print('Peso médio dos jogadores:', round(df['weight'].mean(), 2))  # round para arrendondar com 2 casas decimais
imc = round(df['weight'] / ((df['height'] / 100) ** 2), 2)
df['IMC'] = imc  # nova coluna com valor de IMC atribuida no fim do dataframe
print('maior altura:', df['height'].max(), 'e peso:', df['weight'].max())
print('menor altura:', df['height'].min(), 'e peso:', df['weight'].min())
print('qual estado nasce o maior numero de jogadores')
print(df['birth_state'].value_counts())
print('jogadores mais altos')
print(df.sort_values(by='height'))

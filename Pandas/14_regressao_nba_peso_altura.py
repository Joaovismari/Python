import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
file ='datasets_1358_30676_Players.csv'
nba_df = pd.read_csv(file)
nba_df = nba_df.dropna()#limpando linhas com valores nan
nba_df['age'] = 2021 - nba_df['born']
#regressão linear
x= nba_df[['age','height']]
y= nba_df['weight']
#OLS = ordered list squares,(args = previsão, base)
stat = sm.OLS(y,x).fit()
#print(stat.summary()) #estatisticas dos dados
#print(stat.predict()) #previsões de peso com base nas alturas
#grafico com peso,altura,idade em linha pontilhada conforme altura
plt.figure()
plt.plot(nba_df['height'],nba_df['weight'],'ro')
plt.plot(nba_df['height'],stat.predict(),'ko')
plt.xlabel('altura')
plt.ylabel('peso')
plt.grid()
plt.show()


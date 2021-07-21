import pandas as pd

file = 'datasets_1358_30676_Players.csv'

nba_players = pd.read_csv(file)
print(nba_players)
import pandas as pd

#configurações para visualização de dataframes com mais de 5 colunas no pycharm
desired_width=420
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',20)
#np.set_printoption(linewidth=desired_width) caso seja necessario utilizar o numpy

file = 'Acoes_ficticias.csv'

df = pd.read_csv(file,delimiter=';')#delimitir é o espaçamento
#td = pd.pivot_table(df,index='Papel')#tabela dinâmica com à media por papel
#td = pd.pivot_table(df,columns='Papel')#inverte as linhas colunas
#td = pd.pivot_table(df,index='Papel',values='preco_compra')#setando unica coluna pra view
#td = pd.pivot_table(df,index='Papel',values='Quantidade',aggfunc='sum')#soma dos valores totais
#print(td)

#definindo valor total e preço medio pagos por cada papel de ação
df['valor_total'] =round(df.preco_compra * df.Quantidade,2) # nova coluna
soma_qtd_valor =pd.pivot_table(df,index='Papel',values=['Quantidade','valor_total'],aggfunc='sum')
print(soma_qtd_valor)
soma_qtd_valor['p_medio']= round(soma_qtd_valor.valor_total/soma_qtd_valor.Quantidade,2)
print(soma_qtd_valor)
u'''
Os dicionários representam coleções de dados que contém na sua estrutura um
conjunto de pares chave/valor, nos quais cada chave individual tem um valor associado. Esse
objeto representa a ideia de um mapa, que entendemos como uma coleção associativa desordenada.
A associação nos dicionários é feita por meio de uma chave que faz referência a um valor.
'''

dados_cliente = {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
}

print(dados_cliente['Nome']) # Renan

dados_cliente['Idade'] = 40 # cria uma nova chave e valor no dicionario dados_cliente
dados_cliente.pop('Telefone',None) # remove uma chave do dicionario
del dados_cliente['Idade'] # remove a chave do dicionario

print(dados_cliente)
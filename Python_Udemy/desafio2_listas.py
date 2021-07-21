file_path = 'PIB_100_maiores_cidades_2017.txt'

with open(file_path) as f:
    f_data = f.readlines()
    f.closed

linhas = []

for i in range(len(f_data)):
    linhas.append(f_data[i].split(','))

colunas_dic = {}

for key in linhas[0]:
    colunas_dic[key] = []

    coluna_n = linhas[0].index(key)

    for i in range(1, len(linhas)):  # indice 1,posição 0 são os nomes das colunas
        colunas_dic[key].append(linhas[i][coluna_n])

lista_estados = colunas_dic['Estado']  # filtragem
numero_municipios_SP = lista_estados.count('SP')  # numero de municipios

PIB_acm_sp = 0

for i in range(len(colunas_dic['Estado'])):
    if colunas_dic['Estado'][i] == 'SP':
        PIB_acm_sp += float(colunas_dic['Participação (%)'][i])

print('Numero de Municipios em SP: ', numero_municipios_SP, ' PIB Acumulado: ', PIB_acm_sp, '%')

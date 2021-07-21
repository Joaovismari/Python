# coding: utf-8
#exercicio 1
frase = input('contador de palavras, digite uma frase ')

def contador(frase):
    lista = frase.split(' ')
    n = len(lista)
    print('à frase:', frase,', possui',n,'palavras')

contador(frase)

#exercicio 2
arquivo_path ='Arquivo_sujo.txt'

def numero_palavras(arquivo_path):
    with open(arquivo_path) as f:
        string = f.read()
        f.close

    lista_palavras = string.replace('\n','')#trocar as quebras de linha por nada
    lista_palavras = lista_palavras.split(' ')
    numero = len(lista_palavras)
    print(numero)

numero_palavras(arquivo_path)

#exercicio 3
import imc_calculo as imc

peso,altura = 90,1.81
print(imc.imc_calc(peso,altura))



contador = 0
while (contador <= 5): #faz o teste da condicional
      print(contador)#imprime na tela
      contador = contador + 1# incrementa o valor
else:
      print("loop while encerrado com sucesso!")#não atende a condicional

x = 0
while x < 10:# condicional para disparar o ciclo
    print(x)
    x += 1
    if x == 6: #condicional dentro do ciclo
        print("x é igual a 6, ciclo quebrado")
        break# quebra o ciclo
else:
    print("fim while")# condição inalcançavel
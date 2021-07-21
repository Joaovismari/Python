# exercicio 1, tipo de numero
x = "joao"
if type(x) is str:
    print(x, ' não é um numero')
elif x > 0:
    print(x, " é um numero positivo")
elif x == 0:
    print(x, " é igual à zero")
elif x < 0:
    print(x, " é um numero negativo")
else:
    print(x, " não é um numero")

# exercicio 2, lista intercalada

valores = [1, 2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd', 'e']

nova_lista = []

for i in range(5):
    nova_lista.append(valores[i])
    nova_lista.append(letras[i])

print(nova_lista)

# exercicio 3, fatorial n! = n*n-1..

n = 5
fn = 1

while n > 1:
    fn *= n
    n -= 1
    print(fn)

# desafio 1, 50 primeiro numeros primos

lista_numeros_primos = [2]
proximo_elemento = 2

while len(lista_numeros_primos) < 50:
    proximo_elemento += 1
    proximo_elemento_status = ""

    for elemento in lista_numeros_primos:
        quociente = proximo_elemento / elemento
        quociente_inteiro = proximo_elemento // elemento

        if quociente_inteiro == quociente:
            proximo_elemento_status = "pula"
            break
    if proximo_elemento_status == "pula":
        continue
    else:
        lista_numeros_primos.append(proximo_elemento)

print(len(lista_numeros_primos))
print(lista_numeros_primos)

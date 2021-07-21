# função 1
meu_nome = 'João'

def minha_funcao():
    print('meu nome é ', meu_nome)
    print('Python Anaconda')

minha_funcao()

# função 2
def soma_quadrados(a, b):
    resultado = a ** 2 + b ** 2
    return resultado

n_1 = 3
n_2 = 5

a = soma_quadrados(n_1, n_2)  # atribuindo retorno de uma função à uma variavel
print(a)

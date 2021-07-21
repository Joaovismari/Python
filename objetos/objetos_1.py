class carro:
    def __init__(self,cor,marca,ano):
        self.cor = cor
        self.marca = marca
        self.ano = ano
        self.donos = []

    def add_dono(self,novo_dono):
        self.donos.append(novo_dono)

meu_carro = carro('preto','bmw',2025)
meu_carro.add_dono('João')
meu_carro.add_dono('Marcos')

print(meu_carro.donos)
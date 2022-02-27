# Funcao com Heranca

class Veiculos():
    nome = 'veiculos'
    def __init__(self):
        pass

    def tipo(self):
        return 'Sou um veiculo'


class Carros(Veiculos):
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def acelerar(self):
        return 'Acelerando'


if __name__ == '__main__':
    carro = Carros('Fiat', 'Preta')
    print(carro.acelerar())

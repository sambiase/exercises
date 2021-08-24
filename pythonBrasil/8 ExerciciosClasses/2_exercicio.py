'''
        Classe Quadrado: Crie uma classe que modele um quadrado:

        Atributos: Tamanho do lado
        Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''


class Quadrado:

    def __init__(self,lado):
        self.tamanho_do_lado = lado

    def muda_valor_do_lado(self):
        self.tamanho_do_lado = 20

    def retorna_valor_do_lado(self):
        return self.tamanho_do_lado

    def calcular_area(self):
        return self.tamanho_do_lado ** 2


if __name__ == '__main__':
    quadrado = Quadrado('10')
    print(f'Tamanho do lado Original: {quadrado.tamanho_do_lado}')
    quadrado.muda_valor_do_lado()
    print(f'Tamanho do lado modificado: {quadrado.retorna_valor_do_lado()}')
    print(f'Calcular Área: {quadrado.calcular_area()}')
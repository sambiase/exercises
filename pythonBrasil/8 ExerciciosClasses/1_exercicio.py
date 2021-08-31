'''
        Classe Bola: Crie uma classe que modele uma bola:

        Atributos: Cor, circunferência, material
        Métodos: trocaCor e mostraCor
'''


class Bola:

    def __init__(self,cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        self.cor = 'preto'

    def mostraCor(self):
        print(f'Cor trocada para {self.cor}')


if __name__ == '__main__':
    bola = Bola('amarela',50,'couro')
    bola.trocaCor()
    bola.mostraCor()


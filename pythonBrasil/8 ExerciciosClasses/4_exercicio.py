'''
        Classe Pessoa: Crie uma classe que modele uma pessoa:

        Atributos: nome, idade, peso e altura
        Métodos: Envelhecer, engordar, emagrecer, crescer.

        Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
        ela deve crescer 0,5 cm.
'''


class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1

    def engordar(self):
        pass

    def emagrecer(self):
        pass

    def crescer(self):
        pass


if __name__ == '__main__':
    andre = Pessoa('Andre', 10, 35, 140)
    andre.engordar()
    andre.emagrecer()
    andre.crescer()


for _ in range(22):
    andre.envelhecer()
    print(f'Idade de {andre.nome} é: {andre.idade} anos. E sua altura é {andre.altura} cm')
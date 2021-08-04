class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def print_dados(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'


class Homem(Pessoa):  # Classe HOMEM herda da classe Pai PESSOA
    pass


class Mulher(Pessoa):  # Classe MULHER herda da classe Pai PESSOA
    pass


if __name__ == '__main__':
    homem_1 = Homem(nome='Andre', idade='42')
    print(homem_1.print_dados())
    mulher_1 = Mulher(nome='Flavia', idade='28')
    print(mulher_1.print_dados())
    print(isinstance(homem_1, Pessoa))


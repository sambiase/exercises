'''
    Variavel Global vs Variavel Local
'''


nome = 'Andre'


def variavelLocal():
    global nome
    nome = 'Flavio'
    return nome


if __name__ == '__main__':
    print(f'\nNome da Variavel Global: {nome}')
    print(f'\nNome da Variavel Local: {variavelLocal()}')

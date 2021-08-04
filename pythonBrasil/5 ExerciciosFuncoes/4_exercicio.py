'''
  Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
  se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
'''


def verifica_arg(arg):
    if arg > 0:
        return id('P')
    else:
        return id('N')


if __name__ == '__main__':
    numero = int(input('Digite um numero --> '))
    res = verifica_arg(numero)
    print(res)

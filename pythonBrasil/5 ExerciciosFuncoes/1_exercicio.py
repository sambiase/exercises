'''
    Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

    para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''


def calc(numero):
    for i in range(1, numero + 1):
        for _ in range(i):
            print(f'{i}', end='   ')
        print('')


if __name__ == '__main__':
    numero = int(input('Digite um numero Inteiro --> '))
    calc(numero)
